import requests
import pytest


# from message import Message


@pytest.mark.message_id
def test_select_by_message_id():
    App_URL = "http://127.0.0.1:5000/getMessage"
    headers = {'content-type': 'application/json'}
    params = {'message_id': 'sari'}
    response = requests.post(App_URL, params=params, headers=headers)
    # assert 0
    assert not 'Error' in response.text
    print('\n {}'.format(response.text))
    # assert isinstance(response, Message)


@pytest.mark.application_id
def test_select_message_by_application_id():
    App_URL = "http://127.0.0.1:5000/getMessage"
    headers = {'content-type': 'application/json'}
    params = {'application_id': 8}
    response = requests.post(App_URL, params=params, headers=headers)
    # assert 0
    assert not 'Error' in response.text
    print('\n {}'.format(response.text))
    # print('type {} '.format(type(response).__name__))
    # for i in response:
    #    print('\n {}'.format(i))
    # assert isinstance(i, Message)


#       print('\n {}'.format(i.text))


@pytest.mark.session_id
def test_selecte_message_by_session_id():
    App_URL = "http://127.0.0.1:5000/getMessage"
    headers = {'content-type': 'application/json'}
    params = {'session_id': 'yul'}
    response = requests.post(App_URL, params=params, headers=headers)
    assert not 'Error' in response.text
    print('\n {}'.format(response.text))
    # for i in response:
    # assert isinstance(i, Message)
    # print('\n {}'.format(i.))
