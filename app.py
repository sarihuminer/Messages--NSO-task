from flask import Flask, request
import json
import message
import connect_to_database
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)


@app.route('/sari', methods=["GET", "POST"])
def sari():
    x = request.get_json(force=True)
    x = json.loads(x)
    c = x['application_id']
    return ('ok', 200, get_headers())


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'OPTIONS':
        print('in options')
        cors_enabled_function_auth(request)
    print('index work')
    return 'sari shteren', 200, get_headers()


@app.route('/try')
def tryit():
    language = request.args.get('language')
    framework = request.args['framework']
    website = request.args.get('website')
    return '''<h1>the language is {}</h1>'
    <h1>the frame work is {}</h1>
    <h1>the website is {}</h1>'''.format(language, framework, website)


@app.route('/json_example', methods=["Post"])
def jsonexample():
    req_data = request.get_json()
    # אם לא מופיע המילה
    language = None
    if 'language' in req_data:
        language = req_data['language']
    framework = req_data['framework']
    python_vertion = req_data['vertion_info']['python']
    example = req_data['examples'][0]
    boolean_test = req_data['boolean_test']

    return '''<h1>
    the language value is{}.
    the framework value is{}.
    the python vertion is{}.
    the example 0 is {}.
    the boolean value is {}.
    <h1>
    '''.format(language, framework, python_vertion, example, boolean_test)


@app.route('/deleteMessage', methods=["POST", "GET"])
def delete():
    x = ''
    conn = connect_to_database.create_connection(connect_to_database.database)
    if (request.args.get("application_Id")):
        x = connect_to_database.delete_message_by_applicationId(conn, request.args.get("application_Id"))
    else:
        if (request.args.get("session_id")):
            x = connect_to_database.delete_message_by_session_id(conn, request.args.get("session_id"))
        else:
            if (request.args.get("message_id")):
                x = connect_to_database.delete_massages_by_message_id(conn, request.args.get("message_id"))
    if ('Error' in x):
        print('error')
        return (x, 400, get_headers())
    else:
        print('good')
        return (x, 200, get_headers())


# if i want to keep my data to sqlite as message object
# Create a new message
@app.route('/addMessage_o', methods=["POST"])  # for local running
def addMessage_o():
    req_data = request.get_json(force=True)
    application_id = req_data.get('application_id')
    session_id = req_data.get('session_id')
    message_id = req_data.get('message_id')
    participants = req_data.get('participants')
    participantss = json.dumps(participants)
    content = req_data.get('content')
    newMessage = message.Message(application_id, session_id, message_id, participantss, content)
    print(newMessage)
    # create a database connection
    conn = connect_to_database.create_connection(connect_to_database.database)
    x = connect_to_database.create_message(conn, newMessage)
    print(x)
    if (isinstance(x, int) == True):
        return ('the new message added Successfully!!!', 200, get_headers())
    else:
        return ('Error!!! {}'.format(x), 400, get_headers())


# if i want to keep my data to sqlite as json
# Create a new message
@app.route('/addMessage', methods=["POST"])  # for local running
def addMessage():
    req_data = request.get_json(force=True)
    # create a database connection
    conn = connect_to_database.create_connection(connect_to_database.database)
    x = connect_to_database.insert_new_message(conn, req_data)
    print(x)
    if (isinstance(x, int) == True):
        return ('the new message added Successfully!!!', 200, get_headers())
    else:
        return ('Error!!! {}'.format(x), 400, get_headers())


# get message
@app.route('/getMessage', methods=["GET", "POST"])
def getMessage():
    x = 0
    conn = connect_to_database.create_connection(connect_to_database.database)
    if (request.args.get("application_Id")):
        x = connect_to_database.select_massages_by_applicationId(conn, request.args.get("application_Id"))
    else:
        if (request.args.get("session_id")):
            x = connect_to_database.select_massages_by_session_id(conn, request.args.get("session_id"))
        else:
            if (request.args.get("message_id")):
                x = connect_to_database.select_massages_by_message_id(conn, request.args.get("message_id"))

                return ('application_id:{} \n session_id:{} \n  message_id:{}  \n participants:{}  \n  content:{}'.
                        format(x.application_id, x.session_id, x.message_id, x.participants, x.content))

    return x, 200, get_headers()


def cors_enabled_function_auth(request):
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Authorization',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }
        return '', 204, headers


def get_headers():
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    }
    return headers


if __name__ == "__main__":
    app.run(debug=True, port=5000)

# print('go to function addMassage')
# with open('data.json') as config_file:
#    data = json.loads(config_file.read())
# print(data)
# addMessage(data)
# getMessage("application_id:1")
