import psycopg2
import time
from psycopg2 import OperationalError

def connect_to_db():
    retries = 10
    delay = 1
    while retries > 0:
        try:
            conn = psycopg2.connect(
                dbname="mydb",
                user="user",
                password="password",
                host="postgres",
                port="5432"
            )
            conn.cursor().execute("SELECT 1")
            return conn
        except OperationalError as e:
            time.sleep(delay)
            retries -= 1
    raise Exception("Could not connect to database after retries")

def create_table(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        )
    """)
    conn.commit()
    cur.close()

def insert_record(conn, name):
    cur = conn.cursor()
    cur.execute("INSERT INTO test_table (name) VALUES (%s)", (name,))
    conn.commit()
    cur.close()

def update_record(conn, id, new_name):
    cur = conn.cursor()
    cur.execute("UPDATE test_table SET name = %s WHERE id = %s", (new_name, id))
    conn.commit()
    cur.close()

def delete_record(conn, id):
    cur = conn.cursor()
    cur.execute("DELETE FROM test_table WHERE id = %s", (id,))
    conn.commit()
    cur.close()

def select_records(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM test_table")
    rows = cur.fetchall()
    cur.close()
    return rows

if __name__ == "__main__":
    conn = connect_to_db()
    create_table(conn)
    insert_record(conn, "Test Name")
    records = select_records(conn)
    print("Records:", records)
    conn.close()