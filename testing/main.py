from request.parsing.from_props import read_properties
import uuid
import json
import requests
from request.request import AtolRequest, Request

request = AtolRequest()
print(f'result = {request.receive_token(method="POST")}')
