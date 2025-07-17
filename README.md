# 🏥 Healthcare Backend Assignment – WhatBytes

## 👤 Developed By:
**Sahil Tariq**  
Backend Developer Assignment Submission – July 2025

---

## 🚀 Tech Stack

- **Framework**: Django, Django REST Framework
- **Auth**: JWT (via `djangorestframework-simplejwt`)
- **Database**: PostgreSQL
- **ORM**: Django ORM
- **Others**: Python-dotenv for environment variables

---

## ✅ Features Implemented

### 1. 🔐 Authentication APIs

| Endpoint | Description |
|----------|-------------|
| `POST /api/auth/register/` | User registration |
| `POST /api/auth/login/` | User login (JWT token) |
| `POST /api/auth/refresh/` | Refresh JWT access token |

### 2. 🧑‍⚕️ Patient Management APIs

| Endpoint | Description |
|----------|-------------|
| `POST /api/patients/` | Add new patient *(JWT required)* |
| `GET /api/patients/` | List your patients *(JWT required)* |

> ⚠️ Other CRUD operations (GET by ID, PUT, DELETE) are partially implemented or pending final testing.

---

## 🩺 Doctor & Mapping Models

- Doctor model: setup complete
- Patient-Doctor mapping: models created
- APIs partially integrated (due to time constraints)

---

## ⚠️ Known Issues

- Token expiry may require you to refresh via `/api/auth/refresh/`
- Some endpoints still under development
- UI or browsable API not included – tested via Postman only

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone HEALTHCARE-BACKEND
cd healthcare-backend

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate  # (Windows)


3. Install Requirements
pip install -r requirements.txt


4. Set Environment Variables
DB_NAME=healthcare_db
DB_USER=healthcare_user
DB_PASSWORD=952655
DB_HOST=localhost
DB_PORT=5432

5. Run Migrations and Server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

 API Testing – Postman
 POST /api/auth/register/
{
  "name": "sahil",
  "email": "sahil@example.com",
  "password": "yourpassword"
}

 Login to Get Token
 POST /api/auth/login/
{
  "email": "sahil@example.com",
  "password": "yourpassword"
}

Use Token to Add Patient
POST /api/patients/
Headers:
  Authorization: Bearer <access_token>
Body:
{
  "name": "John Doe",
  "age": 45,
  "gender": "Male",
  "condition": "Diabetes"
}

Folder Structure (Basic)
healthcare-backend/
├── config/
├── users/
├── patients/
├── doctors/
├── mappings/
├── manage.py
├── requirements.txt
├── README.md

Submission Notes
Project partially complete due to time constraints

JWT and protected endpoints working

Models and basic CRUD setup done

Testing done via Postman
