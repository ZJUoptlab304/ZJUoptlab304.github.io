---
layout: archive
title: "出版"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">所有出版物同样可以在<a href="{{site.author.googlescholar}}"> Google Scholar </a>主页检索得到。</div>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
