from faker import Faker
import random


fake = Faker()

data_user = {'email': fake.email(),
             'password': fake.password() + str(random.choice(range(1, 100000))),
             'name': fake.name() + str(random.choice(range(1, 100000)))}

BASE_URL = 'https://stellarburgers.nomoreparties.site/'
CREATING_UNIQUE_USER_POST = BASE_URL + 'api/auth/register'
LOGIN_USER_POST = BASE_URL + 'api/auth/login'
CREATE_ORDER_POST = BASE_URL + 'api/orders'
DEL_USER_DELETE = BASE_URL + 'api/auth/user'

MESSAGE_USER_EXISTS = "User already exists"
MESSAGE_REQUIRED_FIELD = "Email, password and name are required fields"
MESSAGE_INCORRECT_LOGIN = "email or password are incorrect"
MESSAGE_NOT_INGREDIENT = "Ingredient ids must be provided"
MESSAGE_NOT_AUTH = "You should be authorised"


list_param_reg = [
    (None, 'some99password56', 'some465first55Name89'),
    ('some1login367@yandex.ru', None, 'some465first55Name89'),
    ('some1login367@yandex.ru', 'some465first55Name89', None)]

INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d",
    "61c0c5a71d1f82001bdaaa6f",
    "61c0c5a71d1f82001bdaaa70",
    "61c0c5a71d1f82001bdaaa71"
]

BAD_INGREDIENTS = ("82001b", "c5a71")
