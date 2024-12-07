#!/usr/bin/python3
import mysql.connector

def connect_db():
    """Connect to mysql database server"""
    connection = mysql.connector.connect(
            host="localhost",
            user="ibrahim",
            password="ibra12aji",
            database="ALX_prodev",
    )

    return connection

def stream_users():
    """fetch rows using yield"""
    connection = connect_db()
    cursor = connection.cursor()

    sql = "SELECT * FROM user_data"
    users = cursor.execute(sql)
    print(users)

    columns = ["user_id", "name", "email", "age"]
    row = cursor.fetchone()
    while row:
        #yield {"user_id": row[1], "name": row[2], "email": row[3], "age": row[4]}
        yield dict(zip(columns, row))
