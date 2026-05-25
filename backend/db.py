import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Shreya@123",
    database="business_dashboard"
)

def get_cursor():
    return connection.cursor(dictionary=True)