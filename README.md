# Business Listings Dashboard

## Project Overview

Business Listings Dashboard is a full-stack web application that scrapes business listing data from Sulekha, stores it in a MySQL database, provides APIs using FastAPI, and visualizes business insights using a React dashboard.

The project helps analyze business listings across different cities and categories using interactive charts and analytics.

---

## Tech Stack Used

### Frontend
- React.js
- Axios
- Recharts

### Backend
- FastAPI (Python)

### Database
- MySQL

### Web Scraping
- BeautifulSoup
- Requests
- Pandas

---

## Project Structure

business-dashboard/
│
├── backend/
│   ├── main.py
│   ├── db.py
│   ├── scraper.py
│   ├── insert_csv.py
│   ├── business_listings.csv
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│
├── business_dashboard_dump.sql
└── README.md

Features
Business data scraping from Sulekha
MySQL database integration
FastAPI REST APIs
React-based dashboard
City-wise business count visualization
Category-wise business analytics
Source-wise business count
Interactive charts using Recharts

Scraping Approach
The scraper collects business listing data from Sulekha across multiple cities and categories.
Cities Covered
Mumbai
Pune
Delhi
Bangalore
Hyderabad
Categories Covered
Restaurants
Gyms
Hospitals
Beauty Parlour Services
Scraping Process
Sends requests to Sulekha pages
Parses HTML using BeautifulSoup
Extracts business listing information
Saves data to CSV
Inserts records into MySQL database
