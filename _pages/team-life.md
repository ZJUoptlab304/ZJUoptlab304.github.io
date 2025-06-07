---
layout: archive
title: "课题组生活"
permalink: /team-life/
author_profile: true
---

<style>
.timeline {
  position: relative;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px 0;
}

.timeline-item {
  padding: 10px 20px;
  position: relative;
  background-color: inherit;
  width: 100%;
  margin-bottom: 15px;
}

.timeline-content {
  padding: 8px 25px;
  background-color: white;
  position: relative;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  border-left: 4px solid #1565C0;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.timeline-content:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

.timeline-date {
  color: #1565C0;
  font-size: 1.2em;
  font-weight: 600;
  margin-bottom: 5px;
  display: flex;
  align-items: center;
}

.timeline-date::before {
  content: "🗓️";
  margin-right: 8px;
}

.timeline-description {
  color: #666;
  line-height: 1.5;
  margin-bottom: 8px;
  font-size: 1.05em;
}

.image-gallery {
  display: grid;
  gap: 15px;
  margin-top: 5px;
}

.image-gallery.four-images {
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
}

.image-gallery.single-image {
  grid-template-columns: 1fr;
}

.image-item {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 3px 10px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
  aspect-ratio: 16/9;
}

.image-item:hover {
  transform: scale(1.05);
}

.image-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: filter 0.3s ease;
}

.image-item:hover img {
  filter: brightness(1.1);
}

/* 响应式设计 */
@media screen and (max-width: 768px) {
  .timeline-item {
    padding: 15px 20px;
    margin-bottom: 15px;
  }
  
  .image-gallery.four-images {
    grid-template-columns: 1fr;
    grid-template-rows: auto;
  }
}

.celebration-emoji {
  margin-right: 8px;
}
</style>

<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-content">
      <h3 class="timeline-date">2025年6月</h3>
      <p class="timeline-description">
        <span class="celebration-emoji">🎓</span>祝贺高少华博士、王泽博士顺利毕业！在学术路上取得重要里程碑，愿他们在未来的道路上继续发光发热！
      </p>
      <div class="image-gallery single-image">
        <div class="image-item">
          <img src="/images/team-life/2025-06-07.jpg" alt="2025年6月毕业典礼">
        </div>
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-content">
      <h3 class="timeline-date">2025年4月</h3>
      <p class="timeline-description">
        <span class="celebration-emoji">🌸</span>汪老师与课题组同学前往杭州千岛湖风景区进行团建活动。在美丽的山水间，增进彼此的了解与友谊，为团队注入新的活力。摄影：易中华同学。
      </p>
      <div class="image-gallery four-images">
        <div class="image-item">
          <img src="/images/team-life/2025-04团建.jpg" alt="2025年4月团建活动">
        </div>
        <div class="image-item">
          <img src="/images/team-life/2025-04-千岛湖01.jpg" alt="千岛湖风景1">
        </div>
        <div class="image-item">
          <img src="/images/team-life/2025-04-千岛湖02.jpg" alt="千岛湖风景2">
        </div>
        <div class="image-item">
          <img src="/images/team-life/2025-04-千岛湖03.jpg" alt="千岛湖风景3">
        </div>
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-content">
      <h3 class="timeline-date">2024年6月</h3>
      <p class="timeline-description">
        <span class="celebration-emoji">🎓</span>祝贺孙磊博士、文豪东硕士、刘海斌硕士顺利毕业！又一批优秀的学生踏出校园，走向更广阔的天地，愿他们前程似锦！
      </p>
      <div class="image-gallery single-image">
        <div class="image-item">
          <img src="/images/team-life/2024-06.jpg" alt="2024年6月毕业典礼">
        </div>
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-content">
      <h3 class="timeline-date">2024年4月</h3>
      <p class="timeline-description">
        <span class="celebration-emoji">👥</span>组会后，课题组全体成员合影留念。记录下这美好的时光，见证团队的成长与进步。
      </p>
      <div class="image-gallery single-image">
        <div class="image-item">
          <img src="/images/team-life/2024-04.jpg" alt="2024年4月课题组合影">
        </div>
      </div>
    </div>
  </div>
</div>