---
title: Home
---

## Timothy Fitch 
Applied Computer Science graduate with experience building backend systems, APIs, relational databases, and data-driven applications.

<img src="images/timfitchheadshotfinal.png" alt="Timothy Fitch" width="350">

### About Me

I am an Applied Computer Science graduate from the University of Colorado Boulder with a prior B.A. in Political Science and History from the University of Kansas. I am especially interested in backend development, relational databases, data analysis, and building software that helps people organize information and make better decisions.

Before returning to school, I worked in roles involving data management, outreach coordination, website maintenance, and administrative support. That background shaped how I approach software: I care about clear workflows, reliable systems, readable documentation, and tools that solve practical problems rather than just demonstrate technology.

This portfolio reflects both sides of my experience: the technical foundation I developed through computer science work, and the real-world judgment I bring from working with teams, records, communications, and public-facing systems.

### Core Competencies

- Backend development with Python, Flask, FastAPI, and API-driven workflows
- Relational database design, SQL, SQLAlchemy, and data modeling
- Data structures, algorithms, object-oriented programming, and C++
- Frontend fundamentals with HTML, CSS, JavaScript, and Jinja templates
- Technical collaboration using Git, GitHub, Jira, documentation, and team planning
- Data analysis foundations including statistics, linear algebra, and structured reporting

## Featured Projects

<div class="project-grid">
  {% assign featured_projects = site.data.projects | where: "featured", true | sort: "order" %}
  {% for project in featured_projects %}
    {% include project-card.html project=project %}
  {% endfor %}
</div>

[View all projects](projects.html)

## Contact

I am open to software development, backend, database, and data-focused opportunities.

- Email: [timjosfitch@gmail.com](mailto:timjosfitch@gmail.com)
- University Email: [Timothy.Fitch@colorado.edu](mailto:Timothy.Fitch@colorado.edu)
- GitHub: [github.com/timothyfitch](https://github.com/timothyfitch)


