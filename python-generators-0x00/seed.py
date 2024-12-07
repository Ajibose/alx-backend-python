#!/usr/bin/python3.12
import csv
import mysql.connector
import uuid

def connect_db():
    """Connect to mysql database server"""
    connection = mysql.connector.connect(
            host="localhost",
            user="ibrahim",
            password="ibra12aji",
    )

    return connection

def create_database(connection):
    """Creates a database if it does not exist"""
    cur = connection.cursor()

    sql = "CREATE DATABASE IF NOT EXISTS ALX_prodev"
    cur.execute(sql)
    cur.close()

def connect_to_prodev():
    connection = connect_db()
    cur = connection.cursor()
    cur.execute("USE ALX_prodev")
    cur.close()
    return connection

def create_table(connection):
    """Create table"""
    cur = connection.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL
    )
    """
    cur.execute(sql)
    cur.close()

def fetch_data_csv(file_name):
    """Fetch data from file"""
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            yield row
        


def insert_data(connection, data):
    """Insert data in a table"""
    cur = connection.cursor()

    for row in fetch_data_csv("user_data.csv"):
        name, email, age = row

        cur.execute("SELECT * FROM user_data WHERE email = %s", (email,))
        if cur.fetchone():
            print(f"Record with email {email} already exists. Skipping.")
        else:
            sql = "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)"
            cur.execute(sql, (str(uuid.uuid4()), *row))

    connection.commit()
