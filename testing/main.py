from request.parsing.from_props import read_properties
import uuid
import json
import requests

prop_file = 'resources/props.properties'
props = read_properties(prop_file)

json_file = 'resources/register_test_sell_check.json'

with open(json_file, 'r', errors='ignore', encoding='utf-8') as file:
    json_data = json.load(file)

external_id = uuid.uuid4()
json_data['external_id'] = external_id

login = props['atol.login']
password = props['atol.password']

url = props['url']

GET = f'getToken?login={login}&pass={password}'
url_get_token = url + GET

group_code = props['group.code']
url_post_check = url + group_code

token = props['token']

headers = {
    'Content-type': 'application/json; charset=utf-8;',
    'Token': token
}

# response = requests.get(
#     url=url_get_token
# )

response = requests.post(
    url=url_post_check + '/sell',
    headers=headers,
    json=json_data,
)

print(
    f'''
    Response: {response}\n
    As json: {response.json}\n
    Reason: {response.reason}\n
    Text: {response.text}\n
    '''
)
