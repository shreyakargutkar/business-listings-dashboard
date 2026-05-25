# Business Listings Dashboard

## Project Overview

Business Listings Dashboard is a full-stack web application that scrapes business listing data from Sulekha, stores it in a MySQL database, provides APIs using FastAPI, and visualizes business insights using a React dashboard.

The project helps analyze business listings across different cities and categories through charts and analytics.

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

```txt
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
```

---

## Setup Instructions

### 1. Database Setup

Open MySQL and run:

```sql
CREATE DATABASE business_dashboard;

USE business_dashboard;

CREATE TABLE listing_master (
    id INT AUTO_INCREMENT PRIMARY KEY,
    business_name VARCHAR(255),
    category VARCHAR(255),
    city VARCHAR(255),
    address VARCHAR(255),
    phone VARCHAR(255),
    source VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 2. Backend Setup

Navigate to backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate virtual environment:

#### Mac/Linux
```bash
source venv/bin/activate
```

#### Windows
```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn mysql-connector-python pandas requests beautifulsoup4
```

Run backend server:

```bash
uvicorn main:app --reload
```

Backend runs on:

```txt
http://127.0.0.1:8000
```

API Documentation:

```txt
http://127.0.0.1:8000/docs
```

---

### 3. Frontend Setup

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend runs on:

```txt
http://localhost:5173
```

---

### 4. Scrape Data (Optional)

If starting fresh:

```bash
cd backend
source venv/bin/activate
python scraper.py
python insert_csv.py
```

This will:
- Scrape business listing data from Sulekha
- Store data in CSV format
- Insert records into MySQL database

---

## Features

- Business data scraping from Sulekha
- MySQL database integration
- FastAPI REST APIs
- React dashboard
- City-wise business count visualization
- Category-wise business analytics
- Source-wise business count
- Interactive charts using Recharts

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/insert-listing` | POST | Insert business listing |
| `/city-wise-count` | GET | Get business count by city |
| `/category-wise-count` | GET | Get business count by category |
| `/source-wise-count` | GET | Get business count by source |

---

## Scraping Approach

The scraper collects business listing data from Sulekha across multiple cities and categories.

### Cities Covered
- Mumbai
- Pune
- Delhi
- Bangalore
- Hyderabad

### Categories Covered
- Restaurants
- Gyms
- Hospitals
- Beauty Parlour Services

### Process
1. Sends requests to Sulekha pages  
2. Parses HTML using BeautifulSoup  
3. Extracts business listing information  
4. Saves data to CSV  
5. Inserts records into MySQL database  

---

## Dashboard Features

### Analytics Cards
- Total Cities
- Total Categories
- Total Sources

### Charts
- Bar Chart → City-wise business count  
- Pie Chart → Category-wise distribution  
- Bar Chart → Source-wise business count  

---

## Challenges Faced

### 1. MySQL Connection Issues
Faced database connection problems during setup.

**Solution:** Configured MySQL service and corrected connection settings.

### 2. Frontend and Backend Integration
React frontend initially failed to fetch API data.

**Solution:** Added proper API routes and enabled CORS middleware.

### 3. Missing Listing Information
Some scraped records had missing phone numbers and addresses.

**Solution:** Used `"Not Available"` as default values.

### 4. Managing Data Across Multiple Cities
Handling business listings from different categories and cities.

**Solution:** Structured data into MySQL tables for easy querying.

---

## Future Improvements

- Add search functionality
- Add filters by city/category
- Live scraping option
- Better dashboard UI
- Cloud deployment

---

## Author

**Shreya Kargutkar**  
BTech CSE-AIML
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
