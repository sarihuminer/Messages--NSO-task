import requests
import pytest
from message import Message


@pytest.mark.message_id
def test_select_by_message_id():
    App_URL = "http://127.0.0.1:5000/getMessage"
    headers = {'content-type': 'application/json'}
    params = {'message_id': 's'}
    response = requests.post(App_URL, params=params, headers=headers)
    assert 0
    print('\n {}'.format(response.text))
    assert isinstance(response, Message)


@pytest.mark.application_id
def test_select_message_by_applicatin_id():
    App_URL = "http://127.0.0.1:5000/getMessage"
    headers = {'content-type': 'application/json'}
    params = {'applicatin_id': 2}
    response = requests.post(App_URL, params=params, headers=headers)
    for i in response:
        assert isinstance(i, Message)
 #       print('\n {}'.format(i.text))


@pytest.mark.session_id
def test_selecte_message_by_session_id():
    App_URL = "http://127.0.0.1:5000/getMessage"
    headers = {'content-type': 'application/json'}
    params = {'session_id': 'tt'}
    response = requests.post(App_URL, params=params, headers=headers)
    for i in response:
        assert isinstance(i, Message)
        #print('\n {}'.format(i.))
