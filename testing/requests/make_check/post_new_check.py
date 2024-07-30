import requests


group_code = 'group_code_45498'
login = 'fbcf4290-602c-40e1-bedb-84ff2cda98aa'
password = 'X9yTTzCL'

token = 'ieh3KpTZmrBta7nhoVPduZaRKfAsiprx0uqy5oRRmHPmtx1cEGxxCy-H7ABb56vxO7vPD6LhR2fJyCucGRxHMfvcZWcxHb_wUYrUsGvoXtoZeFUUomrw86UzlDXPCa4h'

url = f'https://online.atol.ru/possystem/v4/{group_code}/sell'

print(f'url = {url}\n')

headers = {
    'Content-type': 'application/json; charset=utf-8;',
    'Token': token
}

data = '''{
    "timestamp":" 30.07.2024 12:05:31",
    "external_id": "01910376-b51e-71fe-8131-8672f99bd9cb",
    "service": {
       "callback_url": "https://charge.eco-nrg.store"
    },
    "receipt": {
       "client": {
          "email": "client@client.ru",
          "phone": "+70002410085",
          "name": "Иванов Иван Иванович",
          "inn": "112233445573"
       },
       "company": {
          "email": "email@evotor.ru",
          "sno": "osn",
          "inn": "2310228986",
          "payment_address": "charge.eco-nrg.store"
       },
       "cashier_inn": "2310228986",
       "cashier": "Антон Чеков",
       "items": [
          {
             "name": "Ваш любимый товар 1",
             "price": 1,
             "quantity": 1.0,
             "measure": 0,
             "sum": 1,
             "payment_method": "full_payment",
             "payment_object": 1,
             "vat": {
                "type": "vat0",
                "sum": 0.0
             },
             "excise": 0.0,
             "mark_quantity": {
                "numerator": 1,
                "denominator": 3
             },
             "mark_processing_mode": "0",
             "mark_code": {
                "gs1m": "010463003407001221CMK45BrhN0WLf"
             },
             "agent_info":  {
                "type": "another",
                "paying_agent": {
                   "operation": "Операция 1",
                   "phones": ["+79999999999"]
                },
                "receive_payments_operator": {
                   "phones": ["+79999999999"]
                },
                "money_transfer_operator": {
                   "phones": ["+79999999999"],
                   "name": "Оператор перевода",
                   "address": "г. Москва, ул. Сказочная д.3",
                   "inn": "112233445573"
                }
             },
             "supplier_info": {
                "phones": [
                   "+79999999999"
                ],
                "name": "Название поставщика",
                "inn": "2310228986"
             },
             "sectoral_item_props":[
                {
                   "date": "18.01.2023",
                   "value": "tm=mdlp&sid=00000000405195&",
                   "number": "123/43",
                   "federal_id": "001"
                }
             ]
          }
       ],
       "payments":[
          {
             "type": 1,
             "sum": 1.0
          }
       ],
       "vats":[
          {
             "type": "vat0",
             "sum": 0.0
          }
       ],
       "sectoral_check_props":[
          {
             "date": "18.02.2023",
             "value": "tm=mdlp&sid=00752852194630&",
             "number": "123/89",
             "federal_id": "002"
          }
       ],
       "additional_check_props": "445334544",
       "total": 1.0,
       "additional_user_props": {
          "name": "название доп реквизита",
          "value": "значение доп реквизита"
       }
    }
}'''
 
response = requests.post(
    url=url,
    headers=headers,
    json=data,
)

print(
    f'''
    Response: {response}\n
    As json: {response.json}\n
    Reason: {response.reason}\n
    Text: {response.text}\n
    '''
)
