---
layout: project
title: Tourneyz
project_id: tourneyz
demo_url: "#local-portfolio-demo"
screenshot_note: These screenshots are from the local portfolio demo version of the app, using the same templates and sample tournament data so the project can be shown without a live PostgreSQL database.
concept_note: These reference mockups helped shape the intended interface and tournament flow.
screenshots:
  - src: images/tourneyz-app-home.png
    alt: Tourneyz running home page
    caption: Home page with navigation, project branding, and tournament entry points.
  - src: images/tourneyz-app-play.png
    alt: Tourneyz play dashboard with sample tournaments
    caption: Play dashboard separating hosted, active, previous, and upcoming games.
  - src: images/tourneyz-app-register.png
    alt: Tourneyz tournament registration page
    caption: Tournament registration flow using sample open tournament data.
  - src: images/tourneyz-app-lobby.png
    alt: Tourneyz tournament lobby page
    caption: Lobby view showing registered players for a selected tournament.
  - src: images/tourneyz-app-spectate.png
    alt: Tourneyz spectate page
    caption: Spectate page for viewing active tournaments.
  - src: images/tourneyz-app-create.png
    alt: Tourneyz create tournament page
    caption: Create tournament form with location and tournament settings.
concepts:
  - src: images/tourneyz-create.jpg
    alt: Tourneyz create tournament concept
    caption: Early create tournament concept.
  - src: images/tourneyz-bracket.jpg
    alt: Tourneyz bracket view concept
    caption: Early tournament bracket concept.
---

### Overview

Tourneyz is a team-built web application for organizing local tournaments. The app supports the basic tournament lifecycle: users can register or log in, create tournaments, browse nearby games, register to play, and view tournament activity.

### What It Demonstrates

This project shows my experience working inside a team codebase with multiple feature areas, shared templates, database models, route logic, and user-facing pages. It also reflects the realities of collaborative coursework: coordinating scope, integrating different contributions, documenting known issues, and preparing a usable MVP within a fixed timeline.

### Project Snapshot

- Built as a collaborative software engineering project for CSPB 3308
- Focused on practical web application development, user workflows, and database-backed features
- Designed for casual competitive events such as cornhole, darts, pool, and video games
- Includes templates, static assets, authentication routes, tournament creation, search, registration, lobby, and bracket-related views

### Local Portfolio Demo
{: #local-portfolio-demo }

For portfolio use, I added a safe local demo runner that renders the website with sample tournament data and does not require PostgreSQL. This avoids the original development startup path, which resets the configured database schema.

```powershell
powershell -ExecutionPolicy Bypass -File .\run_portfolio_demo.ps1
```

Then open:

```text
http://127.0.0.1:5000
```

### Future Improvements

- Move secrets and API keys fully into environment variables
- Remove destructive startup database reset behavior
- Consolidate raw SQL and ORM usage into a cleaner data access pattern
- Improve registration flow from search results
- Complete user account history and tournament progression features
