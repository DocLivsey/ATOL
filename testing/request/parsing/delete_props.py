import os
from typing import Union


def delete_properties(from_file, properties: Union[str, list, tuple]):
    temp_file = 'temp.properties'
    with open(from_file, 'r') as props, open(temp_file, 'w') as temp:
        for prop in props:
            if prop.split('=')[0] not in properties:
                temp.write(prop)
    os.remove(from_file)
    os.rename(temp_file, from_file)


def _test(from_file, properties):
    if __name__ == '__main__':
        delete_properties(from_file, properties)
