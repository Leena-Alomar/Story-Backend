# 📖 Tales

**Tales** is a web platform where users can read, write, review, and manage stories. It’s a full-featured space that allows for the creation, categorization, and feedback on stories. This repository contains the backend of the project.

---

## 📦 Backend Repository Overview

This is the backend service for **Tales**, developed with a RESTful API design, powering all core features including stories, categories, and reviews.

---

## 📋 Table of Contents

- [Commits](#commits)
- [Project Description](#project-description)
- [Tech Stack](#tech-stack)
- [Frontend Repository](#frontend-repository)
- [Deployed Site](#deployed-site)
- [ERD Diagram](#erd-diagram)
- [Routing Table](#routing-table)
- [Installation](#installation)
- [Icebox Features](#icebox-features)

---

## ✅ Commits

- ✅ **25 meaningful commits** are tracked in this repository, ensuring transparency and traceability of development progress.

---

## 📖 Project Description

**Tales** is a single-page application (SPA) where users can:

- Read public stories
- Write and manage their own stories
- Categorize stories for better discovery
- Post and manage reviews on stories

Ideal for aspiring writers, casual readers, and story lovers.

---

## 🛠 Tech Stack

- **Language**: Django
- **Framework**: Django
- **Database**: MongoDB / PostgreSQL (update based on actual)
- **Authentication**: JWT / Sessions (if used)
- **Containerization**: Docker (optional)
- **Other**: REST API

---

## 🌐 Frontend Repository

[Frontend Repo](https://github.com/Leena-Alomar/Story-Frontend)

---

## 🚀 Link to Deployed Site

[Deployed App](//)

---

## 🗺 ERD Diagram

![ERD](https://i.ibb.co/Ngsk2jF2/ERD-PROJECT.png)

---

## 🔁 Routing Table

### 📚 Story Routes

| Method | Route              | Description             |
|--------|--------------------|-------------------------|
| GET    | /stories/          | Get a list of all stories |
| POST   | /stories/          | Create a new story      |
| GET    | /stories/:id/      | Get a single story by ID |
| PUT    | /stories/:id/      | Update a story          |
| DELETE | /stories/:id/      | Delete a story          |

### 🏷 Category Routes

| Method     | Route                         | Description                    |
|------------|-------------------------------|--------------------------------|
| GET        | /stories/:id/category/        | Get the category for a story  |
| POST       | /stories/:id/category/        | Create/assign category        |
| PUT/PATCH  | /stories/:id/category/        | Update the category           |
| DELETE     | /stories/:id/category/        | Delete the category           |

### 📝 Review Routes

| Method     | Route                        | Description                   |
|------------|------------------------------|-------------------------------|
| GET        | /stories/:id/reviews/        | Get all reviews for a story  |
| POST       | /stories/:id/reviews/        | Add a new review             |
| GET        | /reviews/:id/                | Get a single review          |
| PUT/PATCH  | /reviews/:id/                | Update a review              |
| DELETE     | /reviews/:id/                | Delete a review              |

---

## ⚙️ Installation (Docker)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tales-backend.git
   cd tales-backend
