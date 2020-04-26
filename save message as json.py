import sqlite3
import json
import connect_to_database



def insert_new_message(message):
    conn = connect_to_database.create_connection(connect_to_database.database)
    cur = conn.cursor()
    m = json.loads(message)
    print(type(message))
    cur.execute("insert into messages_tbl values (?, ?)",
                [m.get('message_id'), message])
    conn.commit()
    conn.close()


if __name__ == "__main__":
    with open('data.json') as config_file:
        data = config_file.read()
    insert_new_message(data)
