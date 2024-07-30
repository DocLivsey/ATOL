import requests
from parsing.from_props import read_properties


prop_file = 'props.properties'
props = read_properties(prop_file)

login = props['atol.login']
password = props['atol.password']
GET = f'?login={login}&pass={password}'
url = props['url.GET'] + GET

print(f'url = {url}\n')

response = requests.get(
    url=url
)

print(
    f'''
    Response: {response}\n
    As json: {response.json}\n
    Reason: {response.reason}\n
    Text: {response.text}\n
    '''
)
