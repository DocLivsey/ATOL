import _io
import json
import uuid
from typing import Union
from structlog import get_logger
import requests
from testing.config import *


class Request:

    __logger = get_logger()

    OK_GREEN = '\033[92m'

    def __init__(
            self,
            url=None,
            headers: dict = None,
            json: Union[str, dict] = None,
            data: Union[str, dict] = None,
            params: Union[str, dict] = None,
            method: str = None
    ):
        self.__url = url
        self.__headers = headers
        self.__json = json
        self.__data = data
        self.__params = params
        self.__method = method
        self.__response = None

    def request_and_response(self, want_to_receive=False):
        self.make_request()
        self.print_response()
        if want_to_receive:
            return self.receive_response()

    def make_request(self):
        if self.__method.lower() == 'post':
            self.__response = requests.post(
                url=self.__url,
                headers=self.__headers,
                json=self.__json,
                data=self.__data,
                params=self.__params,
            )
        elif self.__method.lower() == 'get':
            self.__response = requests.get(
                url=self.__url,
                headers=self.__headers,
                json=self.__json,
                data=self.__data,
                params=self.__params,
            )
        elif self.__method.lower() == 'put':
            self.__response = requests.put(
                url=self.__url,
                headers=self.__headers,
                json=self.__json,
                data=self.__data,
                params=self.__params,
            )
        elif self.__method.lower() == 'delete':
            self.__response = requests.delete(
                url=self.__url,
                headers=self.__headers,
                json=self.__json,
                data=self.__data,
                params=self.__params,
            )

    @staticmethod
    def __response_logger__(function):
        def wrapper(self, *args, **kwargs):
            if self.__response:
                return function(self, *args, **kwargs)
            elif self.__response is None:
                self.__logger.exception(f'before taking response you should make request')
            else:
                if self.__response.status_code == 400:
                    self.__logger.exception('Bad request')
                elif self.__response.status_code == 401:
                    self.__logger.exception('Unauthorized or invalid login or password')
                elif self.__response.status_code == 404:
                    self.__logger.error('Not found')
        return wrapper

    @__response_logger__
    def print_response(self):
        print(
            self.OK_GREEN +
            f'''
            Response: {self.__response}\n
            As json: {self.__response.json()}\n
            Reason: {self.__response.reason}\n
            Text: {self.__response.text}\n
            '''
        )

    @__response_logger__
    def receive_response(self):
        return self.__response


class AtolRequest:

    __ATOL_URL = properties_data[ATOL_URL]
    __ATOL_GET_TOKEN_URL = __ATOL_URL + 'getToken'
    __ATOL_LOGIN = properties_data[ATOL_LOGIN]
    __ATOL_PASSWORD = properties_data[ATOL_PASSWORD]
    __GROUP_CODE = properties_data[GROUP_CODE]
    __TOKEN = properties_data[TOKEN]

    def __init__(
            self,
            atol_url=__ATOL_URL,
            atol_login=__ATOL_LOGIN,
            atol_password=__ATOL_PASSWORD,
            group_code=__GROUP_CODE,
            token=__TOKEN,

    ):
        self.__ATOL_URL = atol_url
        self.__ATOL_GET_TOKEN_URL = atol_url + 'getToken'
        self.__ATOL_LOGIN = atol_login
        self.__ATOL_PASSWORD = atol_password
        self.__GROUP_CODE = group_code
        self.__TOKEN = token

    def receive_token(self, method: str = 'GET'):
        url = self.__ATOL_GET_TOKEN_URL
        headers = {
            'Content-type': 'application/json; charset=utf-8;',
        }
        json = None
        if method.lower() == 'get':
            url += f'?login={self.__ATOL_LOGIN}&pass={self.__ATOL_PASSWORD}'
        elif method.lower() == 'post':
            json = {
                'login': self.__ATOL_LOGIN,
                'pass': self.__ATOL_PASSWORD,
            }
        request = Request(
            url=url,
            headers=headers,
            json=json,
            method=method,
        )
        response = request.request_and_response(want_to_receive=True)
        token = response.json()['token']
        self.__TOKEN = token
        return token

    def register_new_cheque(
            self,
            method: str = 'POST',
            operation: str = 'sell',
            cheque_as_json: Union[str, dict, _io.TextIOWrapper] = None,
            create_uuid_automaticly=False,
    ):
        if type(cheque_as_json) is str:
            if cheque_as_json.endswith('.json'):
                with open(cheque_as_json, 'r', encoding='utf-8') as json_file:
                    cheque_as_json = json.load(json_file)
            else:
                cheque_as_json = json.loads(cheque_as_json)
        elif type(cheque_as_json) is _io.TextIOWrapper:
            cheque_as_json = json.load(cheque_as_json)
        url = f'{self.__ATOL_URL}{self.__GROUP_CODE}/{operation}'
        headers = {
            'Content-type': 'application/json; charset=utf-8;',
            'Token': self.__TOKEN
        }
        if create_uuid_automaticly:
            cheque_as_json['external_id'] = uuid.uuid4().__str__()
        request = Request(
            url=url,
            headers=headers,
            json=cheque_as_json,
            method=method,
        )
        request.request_and_response(want_to_receive=True)
