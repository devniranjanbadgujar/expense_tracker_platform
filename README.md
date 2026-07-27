# Expense Tracker Platform

A full-stack Expense Tracker application built using Flask, React, PostgreSQL and Docker.

---

## Tech Stack

Frontend
- React
- Vite

Backend
- Flask
- SQLAlchemy

Database
- PostgreSQL

Containerization
- Docker
- Docker Compose

---

## Features

- Create Expense
- View Expenses
- Update Expense
- Delete Expense
- Loading State
- Error Handling
- Empty State

---

## Project Structure

frontend/

backend/

compose/

---

## Run

docker compose up --build

---

## API

POST /expenses

GET /expenses

PUT /expenses/{id}

DELETE /expenses/{id}

---
## API

### GET /expenses

Returns all expenses.

---

### POST /expenses

Request

```json
{
    "title":"Laptop",
    "amount":50000,
    "category":"Electronics"
}
```

---

### PUT /expenses/1

Updates an expense.

---

### DELETE /expenses/1

Deletes an expense.


## Architecture Diagram

                React

                  │

         HTTP REST API

                  │

               Flask

                  │

           SQLAlchemy ORM

                  │

            PostgreSQL

                  │

           Docker Volume

## Future Improvements

Authentication

Search

Pagination

Charts

Kubernetes Deployment