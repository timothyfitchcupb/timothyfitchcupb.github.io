---
layout: project
title: Healthcare Worker Advocacy CRM
project_id: healthcare-crm
screenshot_note: These screenshots show the backend workflow from API interaction to reporting and export.
screenshots:
  - src: images/demo-api.png
    alt: Healthcare CRM API overview
    caption: FastAPI documentation view for the backend service.
  - src: images/demo-create-interaction.png
    alt: Create interaction endpoint
    caption: Creating interaction data through the API workflow.
  - src: images/demo-filter-interactions.png
    alt: Filter interactions endpoint
    caption: Filtering stored records by member or campaign.
  - src: images/demo-report-campaign.png
    alt: Report by campaign endpoint
    caption: Aggregated reporting by campaign.
  - src: images/demo-export-csv.png
    alt: CSV export endpoint
    caption: Exporting interaction data for reporting and analysis.
---

### Overview

The Healthcare Worker Advocacy CRM is a backend system designed to manage and analyze nonprofit advocacy data. It models how organizations track members, campaigns, and interactions using a structured database and API-driven workflow instead of spreadsheets or manual systems.

### Project Snapshot

- Built as a focused backend and database project for CSPB 3112
- Models members, campaigns, and interactions in a relational database
- Supports CRUD operations, filtering, reporting, and CSV export
- Demonstrates an end-to-end data pipeline from input to storage to reporting

### Core Features

- Full CRUD operations for members, campaigns, and interactions
- Filtering queries by member and campaign
- Aggregated reporting endpoints
- CSV export of interaction data
- Local API documentation through FastAPI's `/docs` interface

### Demo and Report

The original detailed demo remains available here:

[View System Demo and Report](demo.html)
