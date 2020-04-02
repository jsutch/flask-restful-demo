from werkzeug.security import safe_str_cmp
from user import User 

# users database
user = [
    {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
]

# map dicts
username_mapping = {u.username for u in users}
userid_mapping = {u.id for u in users}

# authenticate a user
def authenticate(username,password):
    user = username_mapping.get(username, None) # default mapping to None if no user is found
    if user and safe_str_cmp(user.password, password): # safe_str_cmp safer than passwd == mypasswd for
        return user

def identity(payload):
    """
    Unique to Flask JWT. The payload is the contents of the JWT
    """
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

