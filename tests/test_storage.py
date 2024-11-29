import psycopg2
import os

def load_sql(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def setup_database(connection):
    cursor = connection.cursor()
    # Run create_tables.sql
    cursor.execute(load_sql('sql/create_tables.sql'))
    # Insert mock data
    cursor.execute(load_sql('sql/insert_data.sql'))
    connection.commit()
    cursor.close()

def teardown_database(connection):
    cursor = connection.cursor()
    # Run drop_tables.sql
    cursor.execute(load_sql('sql/drop_tables.sql'))
    connection.commit()
    cursor.close()

def test_storage_functionality():
    connection = psycopg2.connect(
        dbname="test_db",
        user="postgres",
        password="password",
        host="localhost"
    )

    try:
        # Setup test database
        setup_database(connection)
        
        # Perform your test logic here
        cursor = connection.cursor()
        cursor.execute(load_sql('sql/query_data.sql'))
        results = cursor.fetchall()
        assert len(results) > 0, "No data found in query!"
        cursor.close()
    
    finally:
        # Teardown database
        teardown_database(connection)
        connection.close()
