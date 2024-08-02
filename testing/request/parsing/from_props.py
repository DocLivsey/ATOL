from structlog import get_logger


__logger = get_logger(__name__)


def read_properties(from_file):
    props = {}
    with open(from_file) as properties:
        for line in properties:
            try:
                k, v = line.split('=')
                props[k] = v.rstrip()
            except Exception as e:
                __logger.exception(f'failed to parse properties line with exception {e} in line "{line}"')
        return props
