from typing import Union
from structlog import get_logger
import requests
from testing.config import *


class Request:

    __logger = get_logger()

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
            self.__response = requests.get(
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

    def print_response(self):
        if self.__response:
            print(
                f'''
                Response: {self.__response}\n
                As json: {self.__response.json()}\n
                Reason: {self.__response.reason}\n
                Text: {self.__response.text}\n
                '''
            )
        else:
            self.__logger.exception(f'before taking response you should make request')

    def receive_response(self):
        if self.__response:
            return self.__response
        else:
            self.__logger.exception(f'before taking response you should make request')


class AtolRequest:
    __ATOL_URL = properties_data[ATOL_URL]
    __ATOL_GET_TOKEN_URL = __ATOL_URL + 'getToken'
    __ATOL_LOGIN = properties_data[ATOL_LOGIN]
    __ATOL_PASSWORD = properties_data[ATOL_PASSWORD]

    def __init__(
            self,
            atol_url=__ATOL_URL,
            atol_login=__ATOL_LOGIN,
            atol_password=__ATOL_PASSWORD,
    ):
        self.__ATOL_URL = atol_url
        self.__ATOL_GET_TOKEN_URL = atol_url + 'getToken'
        self.__ATOL_LOGIN = atol_login
        self.__ATOL_PASSWORD = atol_password

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
        return token

    def register_new_cheque(self, method: str = 'POST'):
        pass
