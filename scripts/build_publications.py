#!/usr/bin/env python3
"""Convert the lab BibTeX bibliography into Jekyll publication data.

Usage:
    python3 scripts/build_publications.py

The script intentionally uses only Python's standard library so it can run in
local previews and GitHub Actions without installing extra packages.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "_bibliography" / "publications.bib"
DEFAULT_OUTPUT = ROOT / "_data" / "publications.json"

LINK_FIELDS = (
    ("doi", "DOI"),
    ("pdf", "PDF"),
    ("code", "Code"),
    ("url", "Website"),
)


def split_top_level(value: str, delimiter: str = ",") -> list[str]:
    """Split text only when outside braces and quoted strings."""
    parts: list[str] = []
    start = 0
    depth = 0
    quoted = False
    escaped = False

    for index, char in enumerate(value):
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"' and depth == 0:
            quoted = not quoted
            continue
        if quoted:
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth = max(0, depth - 1)
        elif char == delimiter and depth == 0:
            parts.append(value[start:index].strip())
            start = index + 1

    tail = value[start:].strip()
    if tail:
        parts.append(tail)
    return parts


def unwrap(value: str) -> str:
    value = value.strip().rstrip(",").strip()
    while len(value) >= 2:
        if value[0] == "{" and value[-1] == "}":
            value = value[1:-1].strip()
        elif value[0] == '"' and value[-1] == '"':
            value = value[1:-1].strip()
        else:
            break
    return value


def clean_tex(value: str) -> str:
    """Handle the small, presentation-oriented LaTeX subset used here."""
    replacements = {
        r"\&": "&",
        r"\%": "%",
        r"\_": "_",
        r"\#": "#",
        "---": "—",
        "--": "–",
    }
    for source, target in replacements.items():
        value = value.replace(source, target)
    value = re.sub(r"\\(?:textit|emph|textbf|textsc)\{([^{}]*)\}", r"\1", value)
    value = value.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", value).strip()


def parse_entries(text: str) -> list[dict[str, object]]:
    text = re.sub(r"(?m)^\s*%.*$", "", text)
    entries: list[dict[str, object]] = []
    index = 0

    while True:
        match = re.search(r"@(\w+)\s*([({])", text[index:], re.IGNORECASE)
        if not match:
            break

        entry_type = match.group(1).lower()
        opener = match.group(2)
        closer = "}" if opener == "{" else ")"
        body_start = index + match.end()
        depth = 1
        quoted = False
        escaped = False
        cursor = body_start

        while cursor < len(text) and depth:
            char = text[cursor]
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quoted = not quoted
            elif not quoted:
                if char == opener:
                    depth += 1
                elif char == closer:
                    depth -= 1
            cursor += 1

        if depth:
            raise ValueError(f"Unclosed BibTeX entry near character {body_start}")

        body = text[body_start : cursor - 1].strip()
        index = cursor
        chunks = split_top_level(body)
        if not chunks:
            continue

        key = chunks[0].strip()
        if not key:
            raise ValueError("A BibTeX entry is missing its citation key")

        fields: dict[str, str] = {}
        for chunk in chunks[1:]:
            if not chunk:
                continue
            field_match = re.match(r"([\w-]+)\s*=\s*(.*)\Z", chunk, re.DOTALL)
            if not field_match:
                raise ValueError(f"Invalid field in {key}: {chunk[:80]}")
            name = field_match.group(1).lower()
            fields[name] = clean_tex(unwrap(field_match.group(2)))

        entries.append({"key": key, "type": entry_type, "fields": fields})

    return entries


def is_owner(author: str) -> bool:
    normalized = re.sub(r"[^a-z]", "", author.lower())
    return normalized in {"wangk", "kwang", "wangkaiwei", "kaiweiwang"}


def display_author(author: str) -> str:
    author = author.strip()
    if "," in author:
        family, given = [part.strip() for part in author.split(",", 1)]
        return f"{given} {family}".strip()
    return author


def format_bibtex(entry: dict[str, object]) -> str:
    """Return a copy-ready BibTeX block from the normalized source entry."""
    lines = [f"@{entry['type']}{{{entry['key']},"]
    fields = dict(entry["fields"])
    for name, value in fields.items():
        if value:
            lines.append(f"  {name} = {{{value}}},")
    lines.append("}")
    return "\n".join(lines)


def entry_to_publication(entry: dict[str, object], order: int) -> dict[str, object]:
    key = str(entry["key"])
    entry_type = str(entry["type"])
    fields = dict(entry["fields"])

    title = fields.get("title", "").strip()
    year_text = fields.get("year", "").strip()
    if not year_text:
        date_match = re.match(r"(\d{4})", fields.get("date", "").strip())
        if date_match:
            year_text = date_match.group(1)
    if not title or not year_text:
        raise ValueError(f"{key} must contain both title and year")
    try:
        year = int(year_text)
    except ValueError as exc:
        raise ValueError(f"{key} has an invalid year: {year_text}") from exc

    author_text = fields.get("author", "")
    authors = []
    for raw_author in re.split(r"\s+and\s+", author_text, flags=re.IGNORECASE):
        if raw_author.strip():
            displayed = display_author(raw_author)
            authors.append({"name": displayed, "owner": is_owner(displayed)})

    venue = fields.get("venue", "")
    if not venue:
        venue = (
            fields.get("journal")
            or fields.get("journaltitle")
            or fields.get("booktitle")
            or fields.get("publisher", "")
        )
        details = [fields.get(name, "") for name in ("volume", "number", "pages")]
        details = [item for item in details if item]
        if details:
            venue = f"{venue}. {'; '.join(details)}"

    links: list[dict[str, str]] = []
    seen_urls: set[str] = set()
    doi = fields.get("doi", "")
    for field, label in LINK_FIELDS:
        url = fields.get(field, "")
        if not url:
            continue
        if field == "doi" and not url.startswith(("http://", "https://")):
            url = f"https://doi.org/{url}"
        if url not in seen_urls:
            links.append({"label": label, "url": url})
            seen_urls.add(url)

    for custom_link in fields.get("links", "").split("||"):
        custom_link = custom_link.strip()
        if not custom_link:
            continue
        if "::" not in custom_link:
            raise ValueError(f"{key} has an invalid links item: {custom_link}")
        label, url = [part.strip() for part in custom_link.split("::", 1)]
        if url and url not in seen_urls:
            links.append({"label": label or "Link", "url": url})
            seen_urls.add(url)

    return {
        "key": key,
        "type": entry_type,
        "title": title,
        "year": year,
        "authors": authors,
        "venue": venue,
        "award": fields.get("award", ""),
        "links": links,
        "bibtex": format_bibtex(entry),
        "order": order,
    }


def build_data(entries: list[dict[str, object]]) -> dict[str, object]:
    seen_keys: set[str] = set()
    publications = []
    for order, entry in enumerate(entries):
        key = str(entry["key"])
        if key in seen_keys:
            raise ValueError(f"Duplicate BibTeX key: {key}")
        seen_keys.add(key)
        publications.append(entry_to_publication(entry, order))

    publications.sort(key=lambda item: (-int(item["year"]), int(item["order"])))
    groups: list[dict[str, object]] = []
    for publication in publications:
        if not groups or groups[-1]["year"] != publication["year"]:
            groups.append({"year": publication["year"], "items": []})
        publication.pop("order", None)
        groups[-1]["items"].append(publication)
    return {"groups": groups, "count": len(publications)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true", help="validate without writing output")
    args = parser.parse_args()

    try:
        entries = parse_entries(args.input.read_text(encoding="utf-8"))
        data = build_data(entries)
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if not args.check:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Generated {args.output} from {data['count']} publications.")
    else:
        print(f"Validated {data['count']} publications in {args.input}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
