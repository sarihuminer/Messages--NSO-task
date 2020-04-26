import sqlite3
from sqlite3 import Error
import message
import json

database = r"C:\Users\sari\Documents\year3\task nso\python flask\db\messages.db"


def main():
    database = r"C:\Users\sari\Documents\year3\task nso\python flask\db\messages.db"

    # create a database connection
    conn = create_connection(database)
    # x = select_massages_by_applicationId(conn, 1)
    x = delete_massages_by_message_id(conn, "cc")
    # x = select_massages_by_session_id(conn, "ff")
    print(x)
    # select_massages_by_message_id(conn, "cc")
    # select_massages_by_applicationId(conn, 1)
    # with conn:
    # create a new message
    # newMessage = '{"application_id": 30,"session_id": "aaaa", "message_id": "bbbb","participants": ["avi aviv","moshe cohen"], "content": "Hi, how are you today?"}'


# data = json.loads(newMessage)
# application_id = data.get('application_id')
# session_id = data.get('session_id')
# message_id = data.get('message_id')
# participants = data.get('participants')
# participantss = json.dumps(participants)
# content = data.get('content')
# newMessage = message.Message(application_id, session_id, message_id, participantss, content)
# message_id = create_message(conn, newMessage)
# print(message_id)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_message(conn, message):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO messages(application_id,session_id,message_id,participants,content)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    try:
        cur.execute(sql,
                    (message.application_id, message.session_id, message.message_id, message.participants,
                     message.content))
    except sqlite3.OperationalError as msg:
        print(msg)
        return 'Eror! it is not succeeded to insert the new message!!!!'
    conn.commit()
    return cur.lastrowid


def delete_massages_by_message_id(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql1 = 'select * from messages2'
    sql2 = 'DELETE FROM messages2 WHERE message_id=?'

    cur = conn.cursor()
    try:
        x = cur.execute(sql1, (str(id),))
        data = x.fetchall()
        messages = []
        for d in data:
            # take the json objecct
            selectedData = d[1]
            # take the json values
            selectedData = json.loads(selectedData)
            if selectedData['message_id'] == str(id):
                x = cur.execute(sql2, (str(id),))
    except sqlite3.OperationalError as msg:
        print(msg)
        return 'Eror! it is not succeeded to delete this  message!!!!'
    conn.commit()
    return cur.lastrowid


def delete_message_by_applicationId(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM messages2 WHERE application_Id=?'
    cur = conn.cursor()
    try:
        cur.execute(sql, (int(id),))
    except sqlite3.OperationalError as msg:
        print(msg)
        return 'Eror! it is not succeeded to delete this  message!!!!'
    conn.commit()
    return cur.lastrowid


def delete_message_by_session_id(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql1 = 'select * from messages2'
    sql2 = 'DELETE FROM messages2 WHERE session_id=?'

    cur = conn.cursor()
    try:
        x = cur.execute(sql1, (str(id),))
        data = x.fetchall()
        messages = []
        for d in data:
            # take the json objecct
            selectedData = d[1]
            # take the json values
            selectedData = json.loads(selectedData)
            if selectedData['session_id'] == str(id):
                x = cur.execute(sql2, (str(id),))
    except sqlite3.OperationalError as msg:
        print(msg)
        return 'Eror! it is not succeeded to delete this  message!!!!'
    conn.commit()
    return cur.lastrowid

def select_massages_by_applicationId(conn, applicationId):
    # Select those values, get them to be json
    cur = conn.cursor()
    a = str(applicationId)
    x = cur.execute('select * from messages2 where application_id=?', a)
    data = x.fetchall()
    messages = []
    for d in data:
        # take the json objecct
        selectedData = d[1]
        # take the json values
        selectedData = json.loads(selectedData)
        if selectedData['application_id'] == int(applicationId):
            selectedMessage = message.Message(selectedData['application_id'], selectedData['session_id'],
                                              selectedData['message_id'], selectedData['participants'],
                                              selectedData['content'])

            messages.append(selectedMessage)
    return messages


def select_massages_by_session_id(conn, session_id):
    # Select those values, get them to be json
    cur = conn.cursor()
    a = str(session_id)
    x = cur.execute('select * from messages2')
    data = x.fetchall()
    messages = []
    for d in data:
        # take the json objecct
        selectedData = d[1]
        # take the json values
        selectedData = json.loads(selectedData)
        if selectedData['session_id'] == str(session_id):
            selectedMessage = message.Message(selectedData['application_id'], selectedData['session_id'],
                                              selectedData['message_id'], selectedData['participants'],
                                              selectedData['content'])

            messages.append(selectedMessage)
    return messages


def select_massages_by_message_id(conn, message_id):
    # Select those values, get them to be json
    cur = conn.cursor()
    x = cur.execute('select * from messages2')
    data = x.fetchall()
    for d in data:
        # take the json objecct
        data = d[1]
        # take the json values
        data = json.loads(data)
        if data['message_id'] == message_id:
            break
    # delete this \n from string
    # data = data.replace("\\n", "")
    selectedMessage = message.Message(data['application_id'], data['session_id'],
                                      data['message_id'], data['participants'], data['content'])

    print('selectedMessage:\n application_id:{}\n session_id:{}\n message_id:{}\n participants:{}\n'
          'content:{}\n'.format(selectedMessage.application_id, selectedMessage.session_id
                                , selectedMessage.message_id, selectedMessage.participants, selectedMessage.content))

    return selectedMessage


def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
