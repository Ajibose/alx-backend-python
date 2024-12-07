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

def stream_users_in_batches(batch_size):
    """Fetch data from sql database in batches"""
    conn = connect_db()
    cursor = conn.cursor()

    sql = "SELECT * FROM user_data"
    cursor.execute(sql)

    columns = ["user_id", "name", "email", "age"]
    batch = cursor.fetchmany(batch_size)
    while batch:
        yield list(map(lambda row: dict(zip(columns, row)), batch))
        batch = cursor.fetchmany(batch_size)

def batch_processing(batch_size):
    """Process the batch data"""
    batch_users = stream_users_in_batches(batch_size)

    for batch in batch_users:
        for i, row in enumerate(batch):
            if row['age'] > 25:
                print(row)
