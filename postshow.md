---
layout: project
title: PostShow
project_id: postshow
screenshot_note: These screenshots were captured from the local PostShow app and intentionally include both light and dark mode views.
screenshots:
  - src: images/postshow-home-light.png
    alt: PostShow home page in light mode
    caption: Light-mode landing page with login/signup flow and recent global posts.
  - src: images/postshow-feed-light.png
    alt: PostShow global feed in light mode
    caption: Global feed ordered by actual show date with reusable post cards.
  - src: images/postshow-profile-dark.png
    alt: PostShow profile page in dark mode
    caption: Dark-mode profile page with banner image, avatar, stats, and poster grid.
  - src: images/postshow-share-card-dark.png
    alt: PostShow share card in dark mode
    caption: Dark-mode share-card view built for social sharing experiments.
---

### Overview

PostShow is a personal concert-poster tracking app for saving and sharing shows, festivals, posters, photos, venues, and show memories. It is built as a server-rendered FastAPI application with SQLite persistence, Jinja templates, vanilla JavaScript interactions, and a responsive light/dark interface.

The project is especially relevant to my backend and database interests because the app is more than a static mockup: it stores users, posts, friendships, uploaded media, poster metadata, venue details, and share-card data in a local relational database.

### Project Snapshot

- Built as a local FastAPI and SQLite product prototype
- Uses session-based accounts with password hashing
- Stores users, show posts, carousel images, and friendships in SQLite
- Renders pages with Jinja templates and reusable post-card components
- Includes JSON API routes for post and user data
- Supports both light and dark mode through a persistent theme setting

### Core Features

- Signup, login, logout, editable accounts, profile photos, and banner images
- Show and festival posts with dates, venues, captions, posters, and optional setlists
- Profile pages with grid and feed views
- Friends feed and global feed ordered by actual show date
- Artist, festival, and venue listing pages
- Poster uploads, poster URL support, and carousel image storage
- Drag and zoom image framing for posters, avatars, banners, and carousel images
- Share-card view for creating a social-friendly visual version of a post

### Backend and Data Layer

The backend centers on a `ConcertRepository` class that owns the SQLite queries and returns typed dataclass objects for users, show posts, and images. FastAPI route functions handle page requests, form submissions, file uploads, redirects, and JSON API responses, while the repository keeps database access organized in one place.

The API layer exposes post CRUD routes and user lookup routes, which gives the project a clear path toward a richer frontend or mobile client later.

### Current State

PostShow currently runs as a local FastAPI application with a SQLite database and uploaded media stored under the app's `static/uploads` folder. Optional integrations are structured so they can become live cleanly later: venue lookup can fall back to OpenStreetMap/Nominatim, and setlist.fm lookup waits for an API key while manual setlist entry remains usable.

[View App Breakdown PDF](assets/postshow-app-breakdown.pdf)
