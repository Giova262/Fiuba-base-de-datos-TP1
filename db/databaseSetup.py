from databaseHelper import create_connection, create_table

def setDB():
    # create a database connection
    database = "test.db"
    conn = create_connection(database)

    if conn is None:
        print("Error! Cannot create the database connection.")

    
    # create users table
    create_table(conn)

    return conn