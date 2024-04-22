import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row  # Set the row_factory to sqlite3.Row for dictionary-like access
        print("Connection established.")
    except Error as e:
        print(e)

    return conn


async def execute_query(conn, query):
    """Execute a query on the database."""
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        # Fetch all rows of a query result and convert them to dictionaries
        rows = cursor.fetchall()
        # Convert sqlite3.Row objects to dictionaries
        dict_rows = [dict(row) for row in rows]
        return dict_rows
    except Error as e:
        print(e)
        return None


def list_tables(conn):
    """List all table names in the database."""
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        tables = cursor.fetchall()
        for table in tables:
            print(table[0])  # Print each table name
    except Error as e:
        print(e)


def disconnect(conn):
    conn.close()

