import requests

def test_add_NewMassage():
    App_URL = "http://127.0.0.1:5000/addMessage"
    f = open('../data.json', 'r')
    request_json = f.read()
    headers = {'content-type': 'application/json'}
    response = requests.post(App_URL, request_json, headers=headers)
    print('\n {}'.format(response.text))
    assert not 'Error' in response.text

def test_add_NewMassage_o():
    App_URL = "http://127.0.0.1:5000/addMessage_o"
    f = open('../data.json', 'r')
    request_json = f.read()
    headers = {'content-type': 'application/json'}
    response = requests.post(App_URL, request_json, headers=headers)
    print('\n {}'.format(response.text))
    assert not 'Error' in response.text
