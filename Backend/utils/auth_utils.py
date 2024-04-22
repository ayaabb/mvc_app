import bcrypt
from Backend.FileHandler.read_from_file import get_data

auth_users_path = "database/auth_users.json"

def verify_username(username):
    """
     Verify if a username exists in the authentication database.
     param:  username (str): The username to verify.
     Returns: dict or None: If the username exists, returns the user data dictionary from the authentication database.
                       If the username doesn't exist, returns None.
     """
    users = get_data(auth_users_path)
    if username in users.keys():
        return users[username]
    return None


def verify_password(sorted_password, user_password):
    """
     Verify if a password matches the hashed password stored in the authentication database.
     param: sorted_password (str): The hashed password retrieved from the database.
         user_password (str): The user-provided password to verify.
     Returns: bool: True if the password matches the hashed password, False otherwise.
     """
    return bcrypt.checkpw(user_password.encode('utf-8'), sorted_password.encode('utf-8'))
