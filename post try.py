import requests
import json
payload = {'key1': 'sara'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r)
d = json.loads(r.get_data())
d['altered'] = 'this has been altered...GOOD!'
r.set_data(json.dumps(d))
print('ddd')