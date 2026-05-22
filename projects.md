---
title: Projects
---

## Projects

This portfolio collects software projects that show my work across backend systems, databases, web applications, APIs, and practical data workflows.

<div class="project-grid">
  {% for project in site.data.projects %}
    {% include project-card.html project=project %}
  {% endfor %}
</div>
