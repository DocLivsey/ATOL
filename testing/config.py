from request.parsing.from_props import read_properties
from request.parsing.to_props import rewrite_properties, write_properties
from request.parsing.delete_props import delete_properties


properties_file = 'resources/props.properties'
properties = read_properties(properties_file)


URL = 'url'
TOKEN = 'token'
GROUP_CODE = 'group.code'
ATOL_LOGIN = 'atol.login'
ATOL_PASSWORD = 'atol.password'


__url = properties[URL]
__token = properties[TOKEN]
__group_code = properties[GROUP_CODE]
__atol_login = properties[ATOL_LOGIN]
__atol_password = properties[ATOL_PASSWORD]
