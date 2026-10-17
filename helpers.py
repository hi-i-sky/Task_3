import requests
from constants.urls import USER_URL


def delete_user_by_token(user_access_token):

    headers = {"Authorization": user_access_token}
    r = requests.delete(USER_URL, headers=headers)
    
    return r