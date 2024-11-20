import psycopg2

def connect():
    conn = psycopg2.connect(
        dbname="streamline_db", user="streamline_user", password="streamline_pass", host="localhost"
    )
    return conn
