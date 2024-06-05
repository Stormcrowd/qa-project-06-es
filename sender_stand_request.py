import requests
import data
import configuration



def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body)

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


def get_new_user_token():
    user_response = post_new_user(data.user_body)
    return user_response.json()["authToken"]


def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {auth_token}'
    }

    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                          json=kit_body,
                          headers=headers)





def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

