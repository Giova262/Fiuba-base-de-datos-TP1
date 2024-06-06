import sqlite3
import pandas as pd

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
    sql = '''INSERT INTO users(name, age)
             VALUES(?, ?)'''
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

def pandasVerifyInstallation():
    # Create a DataFrame
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
    df = pd.DataFrame(data)

    # Display the DataFrame
    print(df)

def main():
    database = "test.db"

    print("Starting..")

    pandasVerifyInstallation()

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        # create users table
        create_table(conn)

        # insert users
        user_1 = ('Alice', 30)
        user_2 = ('Bob', 25)
        
        insert_user(conn, user_1)
        insert_user(conn, user_2)

        print("Inserted users successfully.")
        
        # query users
        print("Querying all users:")
        select_all_users(conn)

        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()