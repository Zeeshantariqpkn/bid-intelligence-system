# 🚀 Bid Intelligence System

> A multi-tenant SaaS platform built with Django for managing construction projects, contractor bids, subscriptions, and AI-ready bid analysis.

---

# Overview

Bid Intelligence System is a web-based application designed for construction companies, estimators, contractors, and project managers to organize projects, upload contractor bids, manage organizations, and prepare for intelligent bid analysis.

The system follows a modular architecture and includes user authentication, organization management, project tracking, bid management, subscription plans, REST APIs, and a scalable foundation for future AI-powered document analysis.

---

# Features

## User Authentication

* Email-based authentication
* Secure user registration
* Login & logout
* Password reset
* Django AllAuth integration
* Automatic username generation

---

## Organization Management

* Multi-tenant architecture
* Organization-based data isolation
* Owner, Admin, Member, and Viewer roles
* Organization switching support
* Usage limits based on subscription plans

---

## Project Management

* Create projects
* Edit projects
* Delete projects
* Client management
* Project dashboard
* Project history

---

## Bid Management

* Upload contractor bids
* PDF validation
* Bid item management
* Total bid value calculation
* Bid detail view
* Bid deletion

---

## Risk Analysis

The project includes a dedicated model for bid risk analysis.

It stores:

* Overpriced items
* Underpriced items
* Missing items
* Risk score
* Risk level classification

Risk Levels:

* 🟢 Low
* 🟡 Medium
* 🟠 High
* 🔴 Critical

---

## Subscription System

* Free Plan
* Basic Plan
* Professional Plan
* Enterprise Plan

Supports:

* Trial periods
* Plan upgrades
* Plan downgrades
* Organization limits
* Invoice model
* Stripe-ready architecture

---

## REST API

Built with Django REST Framework.

Includes:

* Project serialization
* Bid serialization
* Bid item serialization
* Dashboard API endpoint
* Session authentication
* Pagination

---

## Security

* Django Authentication
* Django AllAuth
* CSRF Protection
* Session Authentication
* CORS Support
* Secure middleware configuration

---

# Technology Stack

### Backend

* Python
* Django
* Django REST Framework
* Django AllAuth

### Frontend

* HTML5
* Bootstrap 5
* Crispy Forms

### Database

* SQLite (Development)

### Libraries

* django-allauth
* djangorestframework
* crispy-bootstrap5
* django-crispy-forms
* django-cors-headers

---

# Project Structure

```text
apps/
│
├── accounts/
├── api/
├── bids/
├── organizations/
├── projects/
└── subscriptions/

templates/
static/
media/

manage.py
requirements.txt
```

---

# Database Models

## Accounts

* User Authentication

## Organizations

* Organization
* OrganizationMember

## Projects

* Project

## Bids

* Bid
* BidItem
* RiskAnalysis

## Subscriptions

* SubscriptionPlan
* Subscription
* SubscriptionInvoice

---

# Installation

Clone the repository

```bash
git clone https://github.com/Zeeshantariqpkn/bid-intelligence-system.git
```

Move into the project

```bash
cd bid-intelligence-system
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Create an administrator account

```bash
python manage.py createsuperuser
```

Run the development server

```bash
python manage.py runserver
```

Open

```text
http://127.0.0.1:8000
```

---

# Current Capabilities

* Multi-tenant organization management
* Project management
* Bid uploads
* Bid item management
* Risk analysis model
* REST API
* Subscription management
* Authentication
* Role-based architecture

---

# Planned Enhancements

The architecture has been designed to support future enhancements such as:

* AI-powered PDF bid extraction
* OCR for scanned bid documents
* Automatic bid comparison
* Cost anomaly detection
* Contractor ranking
* Bid recommendation engine
* Interactive analytics dashboard
* PostgreSQL production deployment
* Docker support
* Stripe payment processing
* CI/CD pipeline
* Cloud deployment

---

# Screenshots

Add screenshots after deployment.

Recommended images:

```text
screenshots/
├── login.png
├── dashboard.png
├── projects.png
├── upload_bid.png
├── subscriptions.png
└── admin.png
```

---

# Live Demo

Coming Soon

---

# Author

**Zeeshan Tariq**

AI-Assisted Full Stack Developer

Founder & CEO — Datapoch

GitHub: https://github.com/Zeeshantariqpkn

LinkedIn: https://www.linkedin.com/in/zeeshantariqpkn/

---

# License

This project is available for educational, portfolio, and demonstration purposes.
