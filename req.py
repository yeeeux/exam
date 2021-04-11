import requests
import json

url = 'http://127.0.0.1:5000/users?userId=a1b'
param_dict = {'param': 'data'}
# response = requests.get(url, data=json.dumps(param_dict))
response = requests.post(url, data=json.dumps(param_dict))
print(response.json())