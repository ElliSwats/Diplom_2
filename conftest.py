import pytest
import random
from faker import Faker
from methods.request import create_user, del_user, login_user


fake = Faker()


@pytest.fixture
def generate_data_user():
    """Фикстура генерации данных пользователя c использованием Faker и удаления."""
    email = fake.email()
    password = fake.password() + str(random.choice(range(1, 100000)))
    name = fake.name() + str(random.choice(range(1, 100000)))
    data_user = {'email': email, 'password': password, 'name': name}

    yield data_user

    del_response, _ = del_user(email=email, password=password)


@pytest.fixture
def reg_del_user():
    """Фикстура регистрации пользователя использованием Faker и удаления."""
    email = fake.email()
    password = fake.password() + str(random.choice(range(1, 100000)))
    name = fake.name() + str(random.choice(range(1, 100000)))
    register_response, _ = create_user(email=email, password=password, name=name)
    assert register_response.get("success") is True
    access_token = register_response.get("accessToken")
    data_user = {'email': email, 'password': password}

    yield access_token, data_user

    del_response, _ = del_user(email=email, password=password)


@pytest.fixture
def reg_log_del_user():
    """Фикстура регистрации пользователя использованием Faker, авторизации и удаления."""
    email = fake.email()
    password = fake.password() + str(random.choice(range(1, 100000)))
    name = fake.name() + str(random.choice(range(1, 100000)))
    register_response, _ = create_user(email=email, password=password, name=name)
    access_token = register_response.get("accessToken")
    login_user(email=email, password=password)

    yield access_token

    del_response, _ = del_user(email=email, password=password)
