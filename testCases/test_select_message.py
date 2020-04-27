import sys
import requests
import pytest
import pathlib
import json

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
    print('\n {}'.format(response.text))
    assert data['message_id'] == 'sari'


@pytest.mark.application_id
def test_select_message_by_application_id():
    App_URL = "http://127.0.0.1:5000/getMessage"
    headers = {'content-type': 'application/json'}
    params = {'application_id': 9}
    response = requests.post(App_URL, params=params, headers=headers)
    if type(response.text).__name__ == 'str':
        assert not 'Error' in response.text
        print('\n {}'.format(response.text))
    else:
        data = response.text.split("}{")
        for i in data:
            if i[len(i) - 1] != "}":
                i = i + "}"
            elif i[0] != "{":
                i = '{' + i
                i = json.loads(i)
                print('\n {}'.format(i))
                assert int(i['application_id']) == 9


@pytest.mark.session_id
def test_selecte_message_by_session_id():
    App_URL = "http://127.0.0.1:5000/getMessage"
    headers = {'content-type': 'application/json'}
    params = {'session_id': 'qe'}
    response = requests.post(App_URL, params=params, headers=headers)
    if type(response.text).__name__ == 'str':
        assert not 'Error' in response.text
        print('\n {}'.format(response.text))
    else:
        data = response.text.split("}{")
        for i in data:
            if i[len(i) - 1] != "}":
                i = i + "}"
            elif i[0] != "{":
                i = '{' + i
                i = json.loads(i)
                print('\n {}'.format(i))
                assert str(i['session_id']) == 'qe'

