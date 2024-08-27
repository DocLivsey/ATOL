from testing.request.make_cheque.post_new_cheque import post_new_cheque, default_path_to_json
from testing.request.request_token.get_request import get_token


post_new_cheque(default_path_to_json, 'sell', create_uuid_automaticly=True)

#get_token(properties_file='props.properties')
