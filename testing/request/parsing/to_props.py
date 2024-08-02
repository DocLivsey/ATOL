import os

from .delete_props import delete_properties
from structlog import get_logger


__logger = get_logger(__name__)


def write_properties(to_file, properties: dict):
    with open(to_file, 'a') as props:
        for key, value in properties.items():
            props.write(f'{key}={value}\n')


def rewrite_properties(to_file: str, properties: dict):
    temp_file = 'temp.properties'
    with open(to_file, 'r') as props, open(temp_file, 'w') as temp:
        for line in props:
            try:
                k, v = line.split('=')
                if k in properties:
                    temp.write(f'{k}={properties[k]}\n')
                else:
                    temp.write(f'{k}={v}\n')
            except Exception as e:
                __logger.exception(f'failed to parse properties line with exception {e} in line "{line}"')
    os.remove(to_file)
    os.rename(temp_file, to_file)
