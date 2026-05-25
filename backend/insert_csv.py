import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    unix_socket="/tmp/mysql.sock",
    user="root",
    password="Shreya@123",
    database="business_dashboard"
)

cursor = connection.cursor()

df = pd.read_csv("business_listings.csv")

for _, row in df.iterrows():

    query = """
    INSERT INTO listing_master
    (business_name, category, city, address, phone, source)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        row["business_name"],
        row["category"],
        row["city"],
        row["address"],
        row["phone"],
        row["source"]
    )

    cursor.execute(query, values)

connection.commit()

print("500 records inserted successfully")