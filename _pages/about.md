---
permalink: /
title: "汪凯巍课题组简介"
lang: zh
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% for group in site.data.publications.groups %}
  {% for publication in group.items %}
    {% if publication.key == "pub2024_011" %}{% assign featured_cobev = publication %}{% endif %}
    {% if publication.key == "pub2024_002" %}{% assign featured_temporal = publication %}{% endif %}
    {% if publication.key == "pub2025_004" %}{% assign featured_dcdi = publication %}{% endif %}
  {% endfor %}
{% endfor %}

<div class="home-intro">
  <p class="home-intro__eyebrow">浙江大学光电科学与工程学院</p>
  <h2>汪凯巍课题组</h2>
  <ul class="home-intro__highlights">
    <li>研究方向覆盖自动化光学设计、事件相机与计算成像。</li>
    <li>成果发表于 CVPR、ECCV、IEEE TPAMI、TIP、TIV 等重要会议与期刊。</li>
    <li>课题组生活丰富，定期开展春游、聚餐与团建活动。</li>
  </ul>
</div>

<section class="home-featured publications-list" aria-labelledby="home-featured-title">
  <div class="home-featured__heading">
    <div>
      <p class="home-featured__eyebrow">SELECTED PUBLICATIONS</p>
      <h2 id="home-featured-title">精选论文</h2>
    </div>
    <a href="{{ '/publications/' | relative_url }}">查看全部 <span aria-hidden="true">→</span></a>
  </div>

  <div class="home-featured__list">
    <article class="featured-paper">
      <div class="featured-paper__thumb">
        <img src="{{ '/images/publications/featured/cobev.jpg' | relative_url }}" alt="Cobev 论文缩略图" onerror="this.hidden=true">
        <span class="featured-paper__placeholder" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="M7 35V13h34v22H7Z"/><path d="m10 31 9-9 6 6 5-5 8 8M14 18h.01"/></svg><span>论文缩略图</span></span>
      </div>
      <div class="featured-paper__body">
        <div class="featured-paper__meta"><span>IEEE TIP</span><span>2024</span></div>
        <h3><a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=zh-CN&amp;user=B6xWNvgAAAAJ&amp;cstart=20&amp;pagesize=80&amp;citft=1&amp;citft=2&amp;citft=3&amp;email_for_op=guoxf304%40gmail.com&amp;citation_for_view=B6xWNvgAAAAJ:YohjEiUPhakC">Cobev: Elevating roadside 3d object detection with depth and height complementarity</a></h3>
        <p>H. Shi, C. Pang, J. Zhang, K. Yang, et al., <strong>K. Wang</strong></p>
        <div class="publication-actions featured-paper__actions">
          <a class="publication-link" href="https://doi.org/10.1109/TIP.2024.3463409">DOI</a>
          <a class="publication-link" href="https://github.com/MasterHow/CoBEV">GitHub</a>
          <button class="publication-bibtex-toggle" type="button" aria-expanded="false" aria-controls="home-bibtex-pub2024-011" data-bibtex-toggle><span aria-hidden="true">📖</span> BibTeX</button>
        </div>
      </div>
      <div class="publication-bibtex" id="home-bibtex-pub2024-011" data-bibtex-panel hidden>
        <div class="publication-bibtex__header"><span>BibTeX</span><button class="publication-bibtex__copy" type="button" data-bibtex-copy aria-label="复制 CoBEV BibTeX"><span aria-hidden="true">⧉</span><span data-copy-label>复制</span></button></div>
        <pre><code>{{ featured_cobev.bibtex | escape }}</code></pre>
      </div>
    </article>

    <article class="featured-paper">
      <div class="featured-paper__thumb">
        <img src="{{ '/images/publications/featured/temporal-mapping.jpg' | relative_url }}" alt="Temporal-mapping photography for event cameras 论文缩略图" onerror="this.hidden=true">
        <span class="featured-paper__placeholder" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="M7 35V13h34v22H7Z"/><path d="m10 31 9-9 6 6 5-5 8 8M14 18h.01"/></svg><span>论文缩略图</span></span>
      </div>
      <div class="featured-paper__body">
        <div class="featured-paper__meta"><span>ECCV</span><span>2024</span></div>
        <h3><a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=zh-CN&amp;user=B6xWNvgAAAAJ&amp;cstart=20&amp;pagesize=80&amp;citft=1&amp;citft=2&amp;citft=3&amp;email_for_op=guoxf304%40gmail.com&amp;citation_for_view=B6xWNvgAAAAJ:8d8msizDQcsC">Temporal-mapping photography for event cameras</a></h3>
        <p>Y. Bao, L. Sun, Y. Ma, <strong>K. Wang</strong></p>
        <div class="publication-actions featured-paper__actions">
          <a class="publication-link" href="https://doi.org/10.1007/978-3-031-73001-6_4">DOI</a>
          <a class="publication-link" href="https://github.com/YuHanBaozju/EvTemMap">GitHub</a>
          <button class="publication-bibtex-toggle" type="button" aria-expanded="false" aria-controls="home-bibtex-pub2024-002" data-bibtex-toggle><span aria-hidden="true">📖</span> BibTeX</button>
        </div>
      </div>
      <div class="publication-bibtex" id="home-bibtex-pub2024-002" data-bibtex-panel hidden>
        <div class="publication-bibtex__header"><span>BibTeX</span><button class="publication-bibtex__copy" type="button" data-bibtex-copy aria-label="复制 Temporal-mapping BibTeX"><span aria-hidden="true">⧉</span><span data-copy-label>复制</span></button></div>
        <pre><code>{{ featured_temporal.bibtex | escape }}</code></pre>
      </div>
    </article>

    <article class="featured-paper">
      <div class="featured-paper__thumb">
        <img src="{{ '/images/publications/featured/depth-of-field.jpg' | relative_url }}" alt="Towards single-lens controllable depth-of-field imaging 论文缩略图" onerror="this.hidden=true">
        <span class="featured-paper__placeholder" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="M7 35V13h34v22H7Z"/><path d="m10 31 9-9 6 6 5-5 8 8M14 18h.01"/></svg><span>论文缩略图</span></span>
      </div>
      <div class="featured-paper__body">
        <div class="featured-paper__meta"><span>IEEE TCI</span><span>2025</span></div>
        <h3><a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=zh-CN&amp;user=B6xWNvgAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=pubdate&amp;citft=1&amp;citft=2&amp;citft=3&amp;email_for_op=guoxf304%40gmail.com&amp;citation_for_view=B6xWNvgAAAAJ:KbBQZpvPDL4C">Towards single-lens controllable depth-of-field imaging via depth-aware point spread functions</a></h3>
        <p>X. Qian, Q. Jiang, Y. Gao, et al., <strong>K. Wang</strong></p>
        <div class="publication-actions featured-paper__actions">
          <a class="publication-link" href="https://doi.org/10.1109/TCI.2025.3544019">DOI</a>
          <a class="publication-link" href="https://github.com/XiaolongQian/DCDI">GitHub</a>
          <button class="publication-bibtex-toggle" type="button" aria-expanded="false" aria-controls="home-bibtex-pub2025-004" data-bibtex-toggle><span aria-hidden="true">📖</span> BibTeX</button>
        </div>
      </div>
      <div class="publication-bibtex" id="home-bibtex-pub2025-004" data-bibtex-panel hidden>
        <div class="publication-bibtex__header"><span>BibTeX</span><button class="publication-bibtex__copy" type="button" data-bibtex-copy aria-label="复制 DCDI BibTeX"><span aria-hidden="true">⧉</span><span data-copy-label>复制</span></button></div>
        <pre><code>{{ featured_dcdi.bibtex | escape }}</code></pre>
      </div>
    </article>
  </div>
</section>
