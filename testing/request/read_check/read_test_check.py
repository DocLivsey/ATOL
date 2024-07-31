import requests


group_code = 'group_code_45498'
login = 'fbcf4290-602c-40e1-bedb-84ff2cda98aa'
password = 'X9yTTzCL'

token = 'ieh3KpTZmrBta7nhoVPduZaRKfAsiprx0uqy5oRRmHPmtx1cEGxxCy-H7ABb56vxO7vPD6LhR2fJyCucGRxHMfvcZWcxHb_wUYrUsGvoXtoZeFUUomrw86UzlDXPCa4h'

uuid = 'a493ca57-5ff6-473d-8634-f1c5773b698a'

url = f'https://online.atol.ru/possystem/v4/{group_code}/report/{uuid}'

print(f'url = {url}\n')

headers = {
    'Content-type': 'application/json; charset=utf-8;',
    'Token': token
}

response = requests.get(
    url=url,
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
