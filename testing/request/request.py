import requests
from parsing.from_props import read_properties


class Request:

    def __init__(
            self,
            properties='../props.properties',
            url_props_name='url',
            json='./make_check/register_test_sell_check.json',
            method: str = None
    ):
        self.__method = method
        self.__response = None
        self.__load_props__(properties, url_props_name)

    def __load_props__(self, properties, url_props_name):
        props = read_properties(properties)
        self.__url = props[url_props_name]
        self.__headers = {
            'Content-type': 'application/json; charset=utf-8;',
        }
        self.__json = None
        self.__data = None
        self.__params = None

    def request_with_response(self):
        self.make_request()
        self.receive_response()

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

    def receive_response(self):
        print(
            f'''
            Response: {self.__response}\n
            As json: {self.__response.json}\n
            Reason: {self.__response.reason}\n
            Text: {self.__response.text}\n
            '''
        )
