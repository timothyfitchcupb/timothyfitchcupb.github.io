# Healthcare Worker Advocacy CRM

## Overview

This project is a backend system designed to manage and report on nonprofit advocacy data. It models how organizations track members, campaigns, and interactions in a structured database instead of spreadsheets or manual systems.

The focus of the project is backend development, database design, and working with structured data in a practical real-world context.

---

## Current Status

The system is now fully functional as a backend application and supports:

* Full CRUD operations for Members, Campaigns, and Interactions
* Filtering queries (by member and campaign)
* Reporting endpoints (interaction counts by member and campaign)
* CSV export of interaction data
* End-to-end data pipeline from input → storage → query → export

This project is now in the refinement and presentation stage.

---

## Data Model (ER Diagram)

Member (1) ----< Interaction >---- (1) Campaign

### Member

* id (PK)
* name
* email

### Campaign

* id (PK)
* title
* description

### Interaction

* id (PK)
* member_id (FK)
* campaign_id (FK)
* date
* type
* notes

---

## Core Features

* Relational database using SQLite
* ORM models using SQLAlchemy
* FastAPI backend with REST endpoints
* Full CRUD functionality
* Filtering and query support
* Aggregated reporting queries
* CSV export for reporting

---

## API Endpoints (Examples)

### Members

* `GET /members`
* `POST /members`
* `PATCH /members/{id}`
* `DELETE /members/{id}`

### Campaigns

* `GET /campaigns`
* `POST /campaigns`
* `PATCH /campaigns/{id}`
* `DELETE /campaigns/{id}`

### Interactions

* `GET /interactions`
* `POST /interactions`

### Reports

* `/reports/interactions-by-member`
* `/reports/interactions-by-campaign`

### Export

* `/export/interactions.csv`

---

## Technology Stack

* FastAPI
* SQLAlchemy
* SQLite
* Python

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Install backend dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

### 3. Run backend API

```bash
uvicorn app.main:app --reload
```

Open:
http://127.0.0.1:8000/docs

---

### 4. Run project website (Jekyll)

```bash
bundle install
bundle exec jekyll serve
```

Open:
http://localhost:4000

---

## Motivation

Many advocacy and union efforts rely on spreadsheets that are difficult to maintain and use for coordination or reporting. This project explores how a simple purpose-built system can organize that information more effectively.

---

## Project Website

https://timothyfitchcupb.github.io

---

## About Me

I am an Applied Computer Science student at the University of Colorado Boulder with an interest in backend development, databases, and practical data systems.

This project reflects my focus on building tools that organize complex real world data in a clear and usable way.


