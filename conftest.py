import pytest
from methods.request import create_user, del_user, login_user
from data.data import data_user


@pytest.fixture
def generate_data_user():
    """Фикстура генерации данных пользователя c использованием Faker и удаления."""
    email = data_user['email']
    password = data_user['password']
    name = data_user['name']
    data = {'email': email, 'password': password, 'name': name}

    yield data

    del_response, _ = del_user(email=email, password=password)


@pytest.fixture
def reg_del_user():
    """Фикстура регистрации пользователя использованием Faker и удаления."""
    email = data_user['email']
    password = data_user['password']
    name = data_user['name']
    register_response, _ = create_user(email=email, password=password, name=name)
    access_token = register_response.get("accessToken")
    data = {'email': email, 'password': password}

    yield access_token, data

    del_response, _ = del_user(email=email, password=password)


@pytest.fixture
def reg_log_del_user():
    """Фикстура регистрации пользователя использованием Faker, авторизации и удаления."""
    email = data_user['email']
    password = data_user['password']
    name = data_user['name']
    register_response, _ = create_user(email=email, password=password, name=name)
    access_token = register_response.get("accessToken")
    login_user(email=email, password=password)

    yield access_token

    del_response, _ = del_user(email=email, password=password)
