# Healthcare Worker Advocacy CRM
## About This Project

## Overview
This project is a backend system designed to manage and report on nonprofit advocacy data. It models how organizations track members, campaigns, and interactions in a structured database instead of spreadsheets or other less effective manual systems.

The project focuses on backend development, database design, and working with structured data.

## Data Model (ER Diagram)

Member (1) ----< Interaction >---- (1) Campaign

### Member
- id (PK)
- name
- email

### Campaign
- id (PK)
- name
- description

### Interaction
- id (PK)
- member_id (FK)
- campaign_id (FK)
- date
- notes

## Motivation
Many advocacy and union efforts rely on spreadsheets that are difficult to maintain and use for coordination or reporting. This project explores how a simple purposefully built system can organize that information more effectively.

## Core Features
- Relational database for members, campaigns, and interactions
- ORM-based data models using SQLAlchemy
- Backend API routes built with FastAPI
- Create, update, delete, and view records
- Summary reporting and data aggregation
- CSV export of results

## Technology Stack
- FastAPI (backend framework)
- SQLAlchemy (ORM)
- SQLite (development database)
- Python

## Project Status
This is an active course project focused on building a functional backend system with reporting capabilities.

Progress, documentation, and weekly updates are available on the project website.

## Project Website
https://timothyfitchcupb.github.io

-------------------------------------------------

# About Me
I am a Computer Science student at the University of Colorado Boulder with an interest in backend development, data systems, and practical software for real world problems. This project reflects my focus on building reliable systems for organizing complex information in nonprofit and advocacy settings.

