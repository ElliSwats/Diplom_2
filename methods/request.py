import allure
import requests
from data.data import (
    CREATING_UNIQUE_USER_POST,
    LOGIN_USER_POST,
    CREATE_ORDER_POST,
    DEL_USER_DELETE)


@allure.step('регистрация нового пользователя')
def create_user(email, password, name):
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(CREATING_UNIQUE_USER_POST, data=payload)
    return response.json(), response.status_code


@allure.step('Получение access_token')
def get_access_token(email, password):
    payload = {
        "email": email,
        "password": password,
    }
    response = requests.post(url=LOGIN_USER_POST, data=payload)
    return response.json().get("accessToken")


@allure.step('авторизация пользователя')
def login_user(email, password):
    payload = {
        "email": email,
        "password": password
    }
    response = requests.post(LOGIN_USER_POST, data=payload)
    return response.json(), response.status_code


@allure.step('удаление пользователя')
def del_user(email, password):
    access_token = get_access_token(email, password)
    response = requests.delete(DEL_USER_DELETE, headers={'Authorization': access_token})
    return response.json(), response.status_code


@allure.step('создание заказа')
def create_order(ingredients, token):
    payload = {
        "ingredients": ingredients
    }
    response = requests.post(CREATE_ORDER_POST, data=payload, headers={'Authorization': token})
    return response, response.status_code
