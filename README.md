# 🚀 Xeno CRM Backend

<div align="center">

# 🤖 AI-Native Marketing CRM Backend

### Transforming Customer Data into Intelligent Marketing Decisions

<p align="center">
<img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi">
<img src="https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb">
<img src="https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google">
<img src="https://img.shields.io/badge/JWT-Authentication-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">
</p>

### 🎯 Built for Intelligent Customer Engagement, Campaign Automation & AI-Powered Marketing

</div>

---

# 🌟 Project Overview

Xeno CRM Backend is a modern AI-powered marketing CRM platform designed to help businesses intelligently engage with customers using data-driven decision making.

Instead of manually identifying customer audiences, writing campaign messages, selecting communication channels, and analyzing campaign performance, Xeno CRM leverages Artificial Intelligence to assist marketers throughout the entire campaign lifecycle.

The platform combines:

✅ Customer Data Management

✅ Customer Segmentation

✅ Campaign Creation

✅ Communication Tracking

✅ Analytics Reporting

✅ AI-Powered Marketing Assistance

into one unified system.

Built as part of the Xeno Engineering Assignment, the project demonstrates real-world CRM architecture, AI-native workflows, scalable backend design, and production-ready development practices.

---

# 🎯 Problem Statement

Modern brands collect large amounts of customer data.

However, marketers often struggle to answer questions such as:

* Which customers should we target?
* Which customers are becoming inactive?
* What message should we send?
* Which communication channel should we choose?
* Which campaign performs best?
* What actions should be taken next?

Xeno CRM solves these challenges by combining traditional CRM capabilities with AI-driven marketing intelligence.

---

# 🚀 Key Objectives

The backend was designed to:

### 👥 Manage Customer Data

Store and maintain customer information and purchase history.

### 🎯 Build Intelligent Segments

Create highly targeted customer audiences using both manual filters and AI-powered audience generation.

### 📢 Launch Marketing Campaigns

Create, manage, and launch personalized marketing campaigns.

### 📨 Simulate Communication Delivery

Model real-world message delivery lifecycles through a custom-built channel service.

### 📈 Track Campaign Performance

Measure communication effectiveness using detailed campaign analytics.

### 🤖 Provide AI Assistance

Help marketers make better decisions using Gemini-powered recommendations and insights.

---

# 🏗️ System Architecture

```text
                     ┌─────────────────────┐
                     │     Customers       │
                     └──────────┬──────────┘
                                │
                     ┌──────────▼──────────┐
                     │       Orders        │
                     └──────────┬──────────┘
                                │
                     ┌──────────▼──────────┐
                     │      Products       │
                     └──────────┬──────────┘
                                │
                                ▼

                     ┌─────────────────────┐
                     │   MongoDB Atlas     │
                     └──────────┬──────────┘
                                │
                                ▼

                     ┌─────────────────────┐
                     │   FastAPI Backend   │
                     └──────────┬──────────┘
                                │
                                ▼

                     ┌─────────────────────┐
                     │    Gemini AI Layer  │
                     └──────────┬──────────┘

       ┌──────────────────────────────────────────┐
       │                                          │
       ▼                                          ▼

 AI Audience Builder                 AI Segment Suggestions

 AI Message Generator                AI Campaign Advisor

 AI Business Insights                Quick Campaign Creator

       │                                          │
       └──────────────────┬───────────────────────┘
                          ▼

                 Campaign Management

                          ▼

                  Channel Simulation

                          ▼

                Communication Tracking

                          ▼

                  Campaign Analytics
```

---

# 🛠️ Technology Stack

## Backend Framework

* FastAPI
* Uvicorn

## Database

* MongoDB Atlas
* PyMongo

## Authentication & Security

* JWT Authentication
* Passlib
* Bcrypt
* Password Hashing

## Artificial Intelligence

* Google Gemini API

## Validation & Configuration

* Pydantic
* Pydantic Settings
* Python Dotenv

## HTTP & API Clients

* HTTPX
* OpenAI SDK

---

# 📊 Project Statistics

| Category                       | Count |
| ------------------------------ | ----- |
| MongoDB Collections            | 8     |
| Backend Services               | 10    |
| AI Features                    | 6     |
| Authentication APIs            | 3     |
| Core Business Modules          | 10    |
| Communication States           | 6     |
| Analytics Metrics              | 10+   |
| Deployment Platforms Supported | 5+    |

---

# 🗄️ Database Collections

The backend architecture uses eight optimized MongoDB collections.

---

## 👤 Users

Stores CRM user accounts.

### Purpose

* Login
* Authentication
* Authorization
* User Management

---

## 👥 Customers

Stores customer information.

### Data Includes

* Name
* Email
* Phone
* City
* State
* Total Spend
* Total Orders
* Last Order Date
* Customer Status

---

## 📦 Orders

Stores purchase transactions.

### Data Includes

* Order ID
* Customer ID
* Amount
* Category
* Order Date
* Order Status

---

## 🛍️ Products

Stores product catalog information.

### Data Includes

* Product Name
* Category
* Price
* Stock
* Product Status

---

## 🎯 Segments

Stores marketing audiences.

### Examples

* High Value Customers
* Frequent Buyers
* New Customers
* Inactive Customers
* One-Time Buyers

---

## 📢 Campaigns

Stores marketing campaign information.

### Examples

* Summer Sale
* Win Back Campaign
* Loyalty Campaign
* Product Launch Campaign

---

## 📨 Communication Logs

Tracks communication lifecycle events.

### Statuses

* Sent
* Delivered
* Failed
* Opened
* Read
* Clicked

---

## 📈 Campaign Analytics

Stores campaign performance metrics.

### Metrics

* Delivery Rate
* Open Rate
* Read Rate
* Click Rate
* Conversion Rate
* Revenue Generated

---

# 🔐 Authentication Module

The authentication service secures the entire CRM platform.

### Features

✅ User Registration

✅ User Login

✅ JWT Token Generation

✅ Password Hashing

✅ Protected Routes

✅ Current User Retrieval

---

## Authentication APIs

```http
POST /api/auth/register

POST /api/auth/login

GET /api/auth/me
```

---

# 👥 Customer Management Module

Complete CRUD operations for customer records.

### Features

✅ Create Customer

✅ View Customers

✅ Search Customers

✅ Update Customer

✅ Delete Customer

✅ Customer Analytics

---

# 📦 Order Management Module

Tracks customer purchasing activity.

### Features

✅ Create Orders

✅ View Orders

✅ Update Orders

✅ Delete Orders

✅ Revenue Tracking

---

# 🛍️ Product Management Module

Maintains product inventory and catalog information.

### Features

✅ Product Creation

✅ Product Updates

✅ Product Search

✅ Product Management

---

# 🎯 Segment Management Module

Allows marketers to build target audiences.

### Features

✅ Manual Segment Builder

✅ AI Audience Builder

✅ Segment Preview

✅ Audience Count Calculation

---

# 📢 Campaign Management Module

Core marketing engine of the CRM.

### Features

✅ Campaign Creation

✅ Campaign Drafting

✅ Campaign Launching

✅ Campaign Monitoring

✅ Audience Targeting

---

# 📨 Communication Tracking Engine

Models real-world communication delivery systems.

Communication lifecycle:

```text
Sent
 ↓
Delivered
 ↓
Opened
 ↓
Read
 ↓
Clicked
```

or

```text
Sent
 ↓
Failed
```

This mirrors real-world communication providers such as WhatsApp, SMS, Email, and RCS platforms.

---

# ⚡ Channel Service

One of the most important components in the project.

The Xeno assignment specifically required a separate channel simulation service.

Instead of integrating real messaging providers, this service simulates communication outcomes and generates callbacks to the CRM.

### Simulated Events

✅ Delivered

✅ Failed

✅ Opened

✅ Read

✅ Clicked

---

# 📈 Analytics Engine

Provides campaign performance tracking.

### Metrics Tracked

* Total Sent
* Total Delivered
* Total Failed
* Total Opened
* Total Read
* Total Clicked
* Total Conversions
* Revenue Generated
* Delivery Rate
* Open Rate
* Click Rate
* Conversion Rate

---

# 🤖 AI-Native Features

The AI layer is powered by Google Gemini and integrated directly into the CRM workflow.

---

# 🧠 AI Audience Builder

Create customer audiences using natural language.

### Example Prompt

```text
Find customers who spent more than ₹5000
and have not purchased in 60 days.
```

### AI Automatically

✅ Builds Filters

✅ Finds Matching Customers

✅ Calculates Audience Size

✅ Creates Segment

---

# 💡 AI Segment Suggestions

Automatically recommends valuable customer audiences.

### Suggestions

* High Value Customers
* Frequent Buyers
* New Customers
* One-Time Buyers
* Inactive Customers

---

# ✨ AI Message Generator

Generates personalized marketing messages.

### Example Goal

```text
Bring back inactive premium customers.
```

### Example Output

```text
We miss you!

Enjoy 20% OFF on your next purchase.

Come back and explore our latest collection today.
```

---

# 🎯 AI Campaign Advisor

Analyzes campaign history and recommends the most effective communication channel.

### AI Provides

✅ Best Channel

✅ Expected Reach

✅ Recommendation Reasoning

---

# 📊 AI Business Insights

Transforms raw data into actionable recommendations.

Examples:

```text
145 premium customers are currently inactive.

Summer Sale generated the highest revenue.

Suggested Action:
Launch a win-back campaign targeting inactive premium customers.
```

---

# 🚀 Quick Campaign Creator

The Hero AI Feature.

Combines:

* AI Audience Builder
* AI Message Generator
* AI Campaign Advisor

into a single intelligent workflow.

Marketers simply provide a goal and the system prepares an AI-assisted campaign draft.

---

# 📂 Backend Structure

```text
backend/

├── config/
├── models/
├── routes/
├── schemas/
├── services/
├── utils/

├── main.py
├── requirements.txt
└── README.md
```

---

# 📖 API Documentation

FastAPI automatically generates interactive documentation.

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

---

# ⚙️ Local Setup

## Clone Repository

```bash
git clone https://github.com/sp7179/Xeno_CRM_Backend.git
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Environment

```bash
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

```env
MONGODB_URL=your_mongodb_connection

DATABASE_NAME=xeno_crm

JWT_SECRET_KEY=your_jwt_secret

GEMINI_API_KEY=your_gemini_api_key
```

## Start Server

```bash
uvicorn main:app --reload
```

---

# ☁️ Deployment

Recommended Production Stack

```text
Frontend  → Vercel

Backend   → Render

Database  → MongoDB Atlas

AI Layer  → Google Gemini
```

---

# ✅ Xeno Assignment Coverage

| Requirement             | Status |
| ----------------------- | ------ |
| Customer Data Ingestion | ✅      |
| Shopper Segmentation    | ✅      |
| Campaign Creation       | ✅      |
| Communication Tracking  | ✅      |
| Analytics Reporting     | ✅      |
| Channel Simulation      | ✅      |
| AI Integration          | ✅      |
| AI Native Workflow      | ✅      |
| Full Stack Architecture | ✅      |
| Deployment Ready        | ✅      |

---

# 🌟 Highlights

🚀 FastAPI-Powered Architecture

🤖 Gemini AI Integration

🔐 JWT Authentication

📊 Campaign Analytics

📨 Communication Tracking

⚡ Channel Simulation Service

🎯 AI Audience Generation

💡 AI Business Insights

📈 Revenue Analytics

🌐 Production Deployment Ready

---

<div align="center">

# ⭐ If you found this project interesting, don't forget to star the repository!

### Built with ❤️ using FastAPI, MongoDB Atlas, Gemini AI & Modern Backend Engineering.

</div>
