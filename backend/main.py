from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from db import connection, get_cursor
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Listing(BaseModel):
    business_name: str
    category: str
    city: str
    address: str
    phone: str
    source: str


@app.get("/")
def home():
    return {"message": "Business Dashboard API Running"}


@app.post("/insert-listing")
def insert_listing(listing: Listing):
    cursor = get_cursor()

    query = """
    INSERT INTO listing_master
    (business_name, category, city, address, phone, source)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        listing.business_name,
        listing.category,
        listing.city,
        listing.address,
        listing.phone,
        listing.source
    )

    cursor.execute(query, values)
    connection.commit()
    cursor.close()

    return {"message": "Listing inserted successfully"}


@app.get("/city-wise-count")
def city_count():
    cursor = get_cursor()

    query = """
    SELECT city, COUNT(*) as count
    FROM listing_master
    GROUP BY city
    ORDER BY count DESC
    """

    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()

    return data


@app.get("/category-wise-count")
def category_count():
    cursor = get_cursor()

    query = """
    SELECT category, COUNT(*) as count
    FROM listing_master
    GROUP BY category
    ORDER BY count DESC
    """

    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()

    return data


@app.get("/source-wise-count")
def source_count():
    cursor = get_cursor()

    query = """
    SELECT source, COUNT(*) as count
    FROM listing_master
    GROUP BY source
    ORDER BY count DESC
    """

    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()

    return data


@app.get("/top-businesses")
def top_businesses(
    limit: int = Query(10, ge=1, le=100),
    city: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    search: Optional[str] = Query(None)
):
    cursor = get_cursor()

    query = """
    SELECT business_name, city, category, source
    FROM listing_master
    WHERE 1=1
    """
    params = []

    if city:
        query += " AND city = %s"
        params.append(city)
    if category:
        query += " AND category = %s"
        params.append(category)
    if search:
        query += " AND business_name LIKE %s"
        params.append(f"%{search}%")

    query += " ORDER BY id DESC LIMIT %s"
    params.append(limit)

    cursor.execute(query, params)
    data = cursor.fetchall()
    cursor.close()

    return data


@app.get("/cities")
def get_cities():
    cursor = get_cursor()
    query = "SELECT DISTINCT city FROM listing_master ORDER BY city"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return [row["city"] for row in data]


@app.get("/categories")
def get_categories():
    cursor = get_cursor()
    query = "SELECT DISTINCT category FROM listing_master ORDER BY category"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return [row["category"] for row in data]


@app.get("/total-count")
def total_count():
    cursor = get_cursor()
    query = "SELECT COUNT(*) as count FROM listing_master"
    cursor.execute(query)
    data = cursor.fetchone()
    cursor.close()
    return data


@app.get("/filtered-businesses")
def filtered_businesses(
    city: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=200)
):
    cursor = get_cursor()

    query = """
    SELECT business_name, city, category, source
    FROM listing_master
    WHERE 1=1
    """
    params = []

    if city:
        query += " AND city = %s"
        params.append(city)
    if category:
        query += " AND category = %s"
        params.append(category)
    if search:
        query += " AND business_name LIKE %s"
        params.append(f"%{search}%")

    query += " ORDER BY id DESC LIMIT %s"
    params.append(limit)

    cursor.execute(query, params)
    data = cursor.fetchall()
    cursor.close()

    return data