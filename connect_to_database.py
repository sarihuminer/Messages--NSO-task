import sqlite3
from sqlite3 import Error
import message
import json
import pathlib

# when runnig Terminal ,he would know where is the db
path = pathlib.Path(__file__).parent.absolute()
print('p ' + str(path))
path = str(path) + r'\db\messages.db'
database = str(path)
print(database)


# when i check my code by self,before pytest
def main():
    # create a database connection
    conn = create_connection(database)

    # create a new message
    req_data1 = open('./data.json', 'r')
    req_data1 = req_data1.read()
    print(req_data1)
    req_data = json.loads(req_data1)
    application_id = req_data['application_id']
    session_id = req_data['session_id']
    message_id = req_data['message_id']
    participants = req_data['participants']
    participantss = json.dumps(req_data['participants'])
    content = req_data['content']
    newMessage = message.Message(application_id, session_id, message_id, participantss, content)
    # create new message as json
    print('################  insert_new_message ########################')
    x = insert_new_message(conn, req_data)
    print(x)

    # create new message as object
    print('################  insert_new_message ########################')
    x = create_message(conn, newMessage)
    print(x)

    # selected message by applicatin id
    print('################  selected message by application id ########################')
    x = select_massages_by_applicationId(conn, 5)
    print_results(x)
    # selected message by session id
    print('################  selected message by session id ########################')
    x = select_massages_by_session_id(conn, "dd")
    print_results(x)

    # selected message by message id
    print('################  selected message by message id ########################')
    x = select_massages_by_message_id(conn, "y")
    print_results(x)


def print_results(results):
    if str(type(results).__name__) == 'Message':
        print("application_id: {} message_id: {} session_id:{} participants:{} content:{} ".format(
            results.application_id, results.message_id, results.session_id, json.dumps(results.participants),
            results.content), end='/n')
    else:
        for m in results:
            print("application_id: {} message_id: {} session_id:{} participants:{} content:{} ".format(
                m.application_id, m.message_id, m.session_id, json.dumps(m.participants), m.content), end='\n')


# create connection to db
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


# insert new_message
def insert_new_message(conn, message):
    cur = conn.cursor()
    print(type(message))
    m = json.dumps(message)
    print(type(m))
    try:
        cur.execute("insert into messages_tbl values (?, ?)",
                    [message.get('message_id'), m])
    except sqlite3.OperationalError as msg:
        print(msg)
        return ' it is not succeeded to insert the new message!!!!'
    conn.commit()
    return cur.lastrowid


# insert new message as message object
def create_message(conn, message):
    sql = ''' INSERT INTO messages(application_id,session_id,message_id,participants,content)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    try:
        cur.execute(sql,
                    (message.application_id, message.session_id, message.message_id, message.participants,
                     message.content))
    except sqlite3.OperationalError as msg:
        print(msg)
        return ' it is not succeeded to insert the new message!!!!'
    conn.commit()
    return cur.lastrowid


def delete_massages_by_message_id(conn, id):
    sql2 = 'DELETE FROM messages_tbl WHERE message_id=?'
    cur = conn.cursor()
    try:
        cur.execute(sql2, (str(id),))
    except sqlite3.OperationalError as msg:
        print(msg)
        return 'Error! it is not succeeded to delete this  message!!!!'
    conn.commit()
    if not (cur.rowcount <= 0):
        return 'the message deleted successfully!!'
    return 'Error!!!!it did not in our data!!!!'


def delete_message_by_applicationId(conn, id):
    sql1 = 'select * from messages_tbl'
    sql2 = 'DELETE FROM messages_tbl WHERE message_id=?'
    cur = conn.cursor()
    try:
        x = cur.execute(sql1)
        data = x.fetchall()
        messages = []
        for d in data:
            # take the json objecct
            selectedData = d[1]
            # take the json values
            selectedData = json.loads(selectedData)
            if selectedData['application_id'] == int(id):
                x = cur.execute(sql2, (str(selectedData['message_id']),))
    except sqlite3.OperationalError as msg:
        print(msg)
        return 'Error! it is not succeeded to delete this  message!!!!'
    conn.commit()
    if not (cur.rowcount <= 0):
        return 'the message deleted successfully!!'
    return 'Error!!!!it did not in our data!!!!'


def delete_message_by_session_id(conn, id):
    sql1 = 'select * from messages_tbl'
    sql2 = 'DELETE FROM messages_tbl WHERE message_id=?'
    cur = conn.cursor()
    try:
        x = cur.execute(sql1)
        data = x.fetchall()
        messages = []
        for d in data:
            # take the json objecct
            selectedData = d[1]
            # take the json values
            selectedData = json.loads(selectedData)
            if selectedData['session_id'] == str(id):
                x = cur.execute(sql2, (str(selectedData['message_id']),))
    except sqlite3.OperationalError as msg:
        print(msg)
        return 'Error! it is not succeeded to delete this  message!!!!'
    conn.commit()
    if not (cur.rowcount <= 0):
        return 'the message deleted successfully!!'
    return 'Error!!!!it did not in our data!!!!'


def select_massages_by_applicationId(conn, applicationId):
    # Select those values, get them to be json
    cur = conn.cursor()
    a = str(applicationId)
    try:
        x = cur.execute('select * from messages_tbl')
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
        if len(messages) > 0:
            return messages
        return 'Error!!!!it did not in our data!!!!'
    except sqlite3.OperationalError as msg:
        return 'Error! could not faund the message!'


def select_massages_by_session_id(conn, session_id):
    # Select those values, get them to be json
    print('coming ssesion')
    cur = conn.cursor()
    a = str(session_id)
    try:
        x = cur.execute('select * from messages_tbl')
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
        if len(messages) > 0:
            return messages
        return 'Error!!!!it did not in our data!!!!'
    except sqlite3.OperationalError as msg:
        return 'Error! could not faund the message!'


def select_massages_by_message_id(conn, message_id):
    # Select those values, get them to be json
    cur = conn.cursor()
    try:
        x = cur.execute('select * from messages_tbl where message_id=?', (str(message_id),))
        # print(x.fetchall())
        # print(cur.rowcount)
        data = x.fetchall()
        if len(data) == 0:
            return 'Error!!!!it did not in our data!!!!'
        data = json.loads(data[0][1])
        selectedMessage = message.Message(data['application_id'], data['session_id'],
                                          data['message_id'], data['participants'], data['content'])

        print('selectedMessage\n application_id:{}\n session_id:{}\n message_id:{}\n participants:{}\n'
              'content:{}\n'.format(selectedMessage.application_id, selectedMessage.session_id
                                    , selectedMessage.message_id, selectedMessage.participants,
                                    selectedMessage.content))

        return selectedMessage
    except sqlite3.OperationalError as msg:
        return 'Error! could not faund the message!'


if __name__ == '__main__':
    main()
