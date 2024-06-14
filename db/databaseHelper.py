import sqlite3
from logger import Logger

def setDB():
    # create a database connection
    database = "test.db"
    conn = create_connection(database)

    if conn is None:
        Logger.logError("Error! Cannot create the database connection.", None)
    return conn

def closeDB():
    conn.close()

def create_connection(db_file):
    """Create a database connection to an SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        Logger.loginfo(f"SQLite Database connected. Version: {sqlite3.version}")
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn):
    """Create a table in the SQLite database"""
    try:
        sql_create_table = """CREATE TABLE IF NOT EXISTS property_posts (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                start_date TEXT NOT NULL,
                                end_date TEXT,
                                created_on TEXT NOT NULL,
                                lat REAL NOT NULL,
                                lng REAL NOT NULL,
                                province VARCHAR[30] NOT NULL,
                                city VARCHAR[30],
                                operation VARCHAR[10] NOT NULL,
                                type VARCHAR[12] NOT NULL,
                                rooms INTEGER NOT NULL,
                                bedrooms INTEGER NOT NULL,
                                surface_total INTEGER NOT NULL,
                                surface_covered INTEGER,
                                price REAL NOT NULL,
                                currency VARCHAR[4] NOT NULL,
                                title VARCHAR[200] NOT NULL
                             );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        Logger.loginfo("Table created successfully.")
    except sqlite3.Error as e:
        print(e)


def insert_property_post(conn, property_post):
    """Insert a new user into the property_posts table"""
    sql = """INSERT INTO property_posts(start_date, end_date, created_on, lat, lng, province, city, operation, type, rooms, bedrooms, surface_total, surface_covered, price, currency, title)
             VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor = conn.cursor()
    cursor.execute(sql, property_post)
    conn.commit()
    return cursor.lastrowid

def get_count(conn):
    cursor = conn.cursor()
    sql = "SELECT COUNT(*) FROM property_post"
    cursor.execute(sql)
    return cursor.fetchone()[0]
