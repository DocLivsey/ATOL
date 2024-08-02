from request.parsing.from_props import read_properties
from request.parsing.to_props import rewrite_properties, write_properties
from request.parsing.delete_props import delete_properties


properties_file = 'resources/props.properties'
properties_data = read_properties(properties_file)


ATOL_URL = 'atol.url'
TOKEN = 'token'
GROUP_CODE = 'group.code'
ATOL_LOGIN = 'atol.login'
ATOL_PASSWORD = 'atol.password'

