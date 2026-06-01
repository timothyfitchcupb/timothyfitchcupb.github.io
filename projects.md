---
title: Projects
---

## Projects

This portfolio collects software projects that show my work across backend systems, databases, web applications, APIs, and practical data workflows.

<div class="project-grid">
  {% assign ordered_projects = site.data.projects | sort: "order" %}
  {% for project in ordered_projects %}
    {% include project-card.html project=project %}
  {% endfor %}
</div>
