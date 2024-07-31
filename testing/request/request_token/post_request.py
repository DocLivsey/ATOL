import requests
from parsing.from_props import read_properties


prop_file = 'props.properties'
props = read_properties(prop_file)

url = props['url.POST']
login = props['atol.login']
password = props['atol.password']

print(f'url = {url}\n')

headers = {
    'Content-type': 'application/json; charset=utf-8;',
}

data = {
    'login': login,
    'pass': password,
}

response = requests.post(
    url=url,
    data=data,
    headers=headers,
)

print(
    f'''
    Response: {response}\n
    As json: {response.json}\n
    Reason: {response.reason}\n
    Text: {response.text}\n
    '''
)
 