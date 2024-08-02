import _io
import sys
from typing import Union
from structlog import get_logger
from testing.request.request import AtolRequest


__logger = get_logger()

default_path_to_json = ('C:\\Users\\user\\work_folder\\all_scripts\\repos\\doclivsey\\ATOL\\testing\\resources'
                        '\\register_test_sell_check.json')


def post_new_cheque(
        cheque_file: Union[str, dict, _io.TextIOWrapper],
        operation: str,
        create_uuid_automaticly=False,
):
    request = AtolRequest()
    request.register_new_cheque(
        method='POST',
        operation=operation,
        cheque_as_json=cheque_file,
        create_uuid_automaticly=create_uuid_automaticly,
    )


if __name__ == '__main__':
    print(f'args = {sys.argv}')
    try:
        if len(sys.argv) == 1:
            op = sys.argv[1]
            post_new_cheque(default_path_to_json, op)
        elif len(sys.argv) == 2:
            op = sys.argv[1]
            cheque = sys.argv[2]
            post_new_cheque(cheque, op)
    except IndexError:
        __logger.error('No operation')

