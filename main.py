from databaseHelper import (
    create_connection,
    create_table,
    insert_user,
    select_all_users,
)
from pandasHelper import checkData


def main():

    print("Starting..")

    dataForDatabase = checkData()

    # create a database connection
    database = "test.db"
    conn = create_connection(database)

    if conn is not None:
        # create users table
        create_table(conn)

        # insert users
        user_1 = ("Alice", 30)
        user_2 = ("Bob", 25)
        insert_user(conn, user_1)
        insert_user(conn, user_2)
        print("Inserted users successfully.")

        # query users
        print("Querying all users:")
        # select_all_users(conn)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")


if __name__ == "__main__":
    main()
