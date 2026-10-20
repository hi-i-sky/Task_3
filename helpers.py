import requests
from faker import Faker
from constants.urls import USER_URL


def delete_user_by_token(user_access_token):

    headers = {"Authorization": user_access_token}
    r = requests.delete(USER_URL, headers=headers)
    
    return r


def generate_user_payload():
    fake = Faker()
    return {
        'email': fake.email(),
        'password': fake.password(),
        'name': fake.first_name()
    }