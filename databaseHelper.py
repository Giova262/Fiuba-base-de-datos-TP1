import sqlite3


def create_connection(db_file):
    """Create a database connection to an SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"SQLite Database connected. Version: {sqlite3.version}")
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn):
    """Create a table in the SQLite database"""
    try:
        sql_create_table = """CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                age INTEGER
                             );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(e)


def insert_user(conn, user):
    """Insert a new user into the users table"""
    sql = """INSERT INTO users(name, age)
             VALUES(?, ?)"""
    cursor = conn.cursor()
    cursor.execute(sql, user)
    conn.commit()
    return cursor.lastrowid


def select_all_users(conn):
    """Query all rows in the users table"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
