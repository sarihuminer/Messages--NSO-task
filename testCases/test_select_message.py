import sys
import requests
import pytest
import pathlib
import json
import ast

path = pathlib.Path(__file__).parent.absolute()
sys.path.append(path)


@pytest.mark.message_id
def test_select_by_message_id():
    App_URL = "http://127.0.0.1:5000/getMessage"
    headers = {'content-type': 'application/json'}
    params = {'message_id': 'sari'}
    response = requests.post(App_URL, params=params, headers=headers)
    data = response.json()
    assert not 'Error' in response.text
    print_message(data)
    assert data['message_id'] == 'sari'


@pytest.mark.application_id
def test_select_message_by_application_id():
    App_URL = "http://127.0.0.1:5000/getMessage"
    headers = {'content-type': 'application/json'}
    params = {'application_id': 9}
    response = requests.post(App_URL, params=params, headers=headers)
    if type(response.text).__name__ == 'str' and not '{' in response.text:
        assert not 'Error' in response.text
        print('\n {}'.format(response.text))
    else:
        response = json.loads(response.text)
        for message in response:
            m = json.loads(message)
            print_message(m)
    assert int(m['application_id']) == 9


@pytest.mark.session_id
def test_selecte_message_by_session_id():
    App_URL = "http://127.0.0.1:5000/getMessage"
    headers = {'content-type': 'application/json'}
    params = {'session_id': 'qe'}
    response = requests.post(App_URL, params=params, headers=headers)
    if type(response.text).__name__ == 'str' and not '{' in response.text:
        assert not 'Error' in response.text
        print('\n {}'.format(response.text))
    else:
        response = json.loads(response.text)
        for message in response:
            m = json.loads(message)
            print_message(m)
    assert str(m['session_id']) == 'qe'


# print nice message
def print_message(message):
    print("\n application_id: {} message_id: {} session_id:{} participants:{} content:{} ".format(
        message['application_id'], message['message_id'], message['session_id'], json.dumps(message['participants']),
        message['content']), end='\n')
