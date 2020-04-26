import requests
import pytest

@pytest.mark.message_id
def test_delete_message_by_message_id():
    App_URL = "http://127.0.0.1:5000/deleteMessage"
    headers = {'content-type': 'application/json'}
    params = {'message_id': 'rt'}
    response = requests.post(App_URL, params=params, headers=headers)
    #assert 0
    print('\n {}'.format(response.text))
    assert not 'Error' in response.text

@pytest.mark.application_id
def test_delete_message_by_application_id():
    App_URL = "http://127.0.0.1:5000/deleteMessage"
    headers = {'content-type': 'application/json'}
    params = {'application_Id': 1}
    response = requests.post(App_URL, params=params, headers=headers)
    print('\n {}'.format(response.text))
    assert not 'Error' in response.text

@pytest.mark.session_id
def test_delete_message_by_session_id():
    App_URL = "http://127.0.0.1:5000/deleteMessage"
    headers = {'content-type': 'application/json'}
    params = {'session_id': 'dd'}
    response = requests.post(App_URL, params=params, headers=headers)
    print('\n {}'.format(response.text))
    assert not 'Error' in response.text
