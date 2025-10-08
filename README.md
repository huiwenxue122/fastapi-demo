# fastapi-docker-starter

# 🚀 FastAPI Docker Starter

A minimal **FastAPI** project containerized with **Docker**.  
This template helps you quickly build, test, and deploy FastAPI applications in a clean and reproducible environment.

---

## 📖 Overview

This project demonstrates how to:
- Build a RESTful API using **FastAPI**
- Containerize it with **Docker**
- Run and manage it via **Docker Compose**

Whether you are new to FastAPI or learning Docker, this project is a perfect starting point.

---

## 🧠 Features

- ⚡️ FastAPI — a modern, high-performance web framework for building APIs with Python
- 🐳 Dockerized environment — consistent setup across machines
- 🔁 Hot-reload support — ideal for local development
- 📦 Dependency management via `requirements.txt`
- 🧩 Easy to extend — add new routes or services seamlessly

---

## 🏗️ Project Structure

fastapi-docker-starter/
├── main.py # FastAPI application entry
├── requirements.txt # Python dependencies
├── Dockerfile # Build instructions for the image
├── docker-compose.yml # (optional) Compose setup
├── .dockerignore # Files ignored by Docker
└── .gitignore # Files ignored by Git


---

## ⚙️ Run Locally (without Docker)

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run FastAPI
uvicorn main:app --reload
```

🐳 Run with Docker
```
# Build the image
docker build -t fastapi-demo .

# Run the container
docker run -d -p 8080:80 --name fastapi-demo fastapi-demo
```

Then visit 👉 http://localhost:8080/docs

📦 Run with Docker Compose (recommended)
```
docker compose up -d --build


Then check running containers:

docker ps

```
Access the API at 👉 http://localhost:8888/docs

🧰 API Example

Method	Endpoint	Description

GET	/	Root endpoint

GET	/users	Get list of users

POST	/users	Create a new user

