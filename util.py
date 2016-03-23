import base64

def b64_to_key(data):
    return base64.urlsafe_b64decode(data).decode('ascii')

def key_to_b64(key):
    return base64.urlsafe_b64encode(key.encode('ascii'))

def get_url(key):
    return '/item/'+key_to_b64(key).decode('ascii')

