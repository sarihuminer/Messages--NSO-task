import connect_to_database
import sqlite3
from sqlite3 import Error


def main():
    database = r"C:\Users\sari\Documents\year3\task nso\python flask\db\messages.db"

    sql_create_messages_table = """ CREATE TABLE IF NOT EXISTS messages (
                  application_id integer ,
                  session_id text NOT NULL,
                message_id text PRIMARY KEY,
               participants varchar(255),
               content text
        ); """

    sql_create_messages_tbl = """ CREATE TABLE IF NOT EXISTS messages_tbl (
                                                message_id text PRIMARY KEY,
                                                data json
                                            ); """
    # create a database connection
    conn = connect_to_database.create_connection(connect_to_database.database)

    # create tables
    if conn is not None:
        # create messages table
        create_table(conn, sql_create_messages_tbl)
        create_table(conn, sql_create_messages_table)

    else:
        print("Error! cannot create the database connection.")


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == "__main__":
    main()
