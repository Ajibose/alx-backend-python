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


def stream_user_ages():
    """Generatot to get the age"""
    conn = connect_db()
    cur = conn.cursor(dictionary=True)

    try:
        sql = "SELECT * FROM user_data"
        cur.execute(sql)

        user = cur.fetchone()
        while user:
            yield user['age']
            user = cur.fetchone()
    finally:
        cur.close()
        conn.close()


def calculate_average_age():
    """Calculate the average age lazily"""
    ages = stream_user_ages()

    total_age = 0
    user_nums = 0

    for age in ages:
        user_nums += 1
        total_age += age

    print(f"Average age of users: {total_age/user_nums}")


calculate_average_age()
