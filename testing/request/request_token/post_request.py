import sys
from testing.request.request import AtolRequest
from testing.request.parsing.to_props import rewrite_properties


path_to_props = '../../props.properties'


def get_token(properties_file: str):
    request = AtolRequest()
    token = request.receive_token(method='POST')
    print(f'take token: {token}')
    rewrite_properties(properties_file, {'token': token})


if __name__ == '__main__':
    try:
        path_from_sys = sys.argv[1]
        if path_from_sys.endswith('.properties'):
            get_token(path_from_sys)
        else:
            get_token(path_to_props)
    except IndexError:
        get_token(path_to_props)
 