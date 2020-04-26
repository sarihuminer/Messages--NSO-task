import requests
import pytest

@pytest.mark.message_id
def test_delete_message_by_message_id():
    App_URL = "http://127.0.0.1:5000/deleteMessage"
    headers = {'content-type': 'application/json'}
    params = {'message_id': 'a'}
    response = requests.post(App_URL, params=params, headers=headers)
    print('\n {}'.format(response.text))
    assert not 'Error' in response.text

@pytest.mark.application_id
def test_delete_message_by_applicatin_id():
    App_URL = "http://127.0.0.1:5000/deleteMessage"
    headers = {'content-type': 'application/json'}
    params = {'applicatin_id': 1}
    response = requests.post(App_URL, params=params, headers=headers)
    print('\n {}'.format(response.text))
    assert not 'Error' in response.text

@pytest.mark.session_id
def test_delete_message_by_session_id():
    App_URL = "http://127.0.0.1:5000/deleteMessage"
    headers = {'content-type': 'application/json'}
    params = {'session_id': 'gg'}
    response = requests.post(App_URL, params=params, headers=headers)
    print('\n {}'.format(response.text))
    assert not 'Error' in response.text
