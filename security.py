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

username_mapping = {'bob':{
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
}

userid_mapping = {1: {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
}

# authenticate a user
def authenticate(username,password):
    user = username_mapping.get(username, None) # default mapping to None if no user is found
    if user and user.password == password:
        return user

def identity(payload):
    """
    Unique to Flask JWT. The payload is the contents of the JWT
    """
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

