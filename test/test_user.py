import allure
import pytest
from methods.request import create_user, login_user
from data.data import (
    list_param_reg,
    MESSAGE_USER_EXISTS,
    MESSAGE_REQUIRED_FIELD,
    MESSAGE_INCORRECT_LOGIN)


@allure.epic('Класс тестирования пользователей')
class TestUser:

    @allure.title('Тест регистрация пользователя с валидными данными')
    def test_create_user_valid_data_success(self, generate_data_user):
        with allure.step('Подготовка тестовых данных и отправка запроса'):
            data_user = generate_data_user
            register_response, status_code = create_user(
                email=data_user['email'],
                password=data_user['password'],
                name=data_user['name'])
        with allure.step('проверка успешности создания пользователя'):
            assert status_code == 200 and register_response["success"] is True

    @allure.title('Тест невозможности повторной регистрации')
    def test_re_registration_user_data_negative(self, generate_data_user):
        with allure.step('Подготовка тестовых данных и отправка запроса'):
            data_user = generate_data_user
            register_response, status_code = create_user(
                email=data_user['email'],
                password=data_user['password'],
                name=data_user['name'])
        with allure.step('проверка успешного создания пользователя'):
            assert status_code == 200 and register_response["success"] is True
        with allure.step('отправка запроса на повторную регистрацию'):
            re_register_response, re_status_code = create_user(
                email=data_user['email'],
                password=data_user['password'],
                name=data_user['name'])
        with allure.step('проверка невозможности создания пользователя'):
            assert re_status_code == 403
            assert re_register_response["success"] is False and re_register_response["message"] == MESSAGE_USER_EXISTS

    @allure.title('Тест создания пользователя с неполными данными')
    @pytest.mark.parametrize('email, password, name', list_param_reg)
    def test_create_user_without_required_field(self, email, password, name):
        with allure.step('отправка запроса'):
            register_response, status_code = create_user(
                email=email,
                password=password,
                name=name)
        with allure.step('проверка невозможности создания пользователя без полных данных'):
            assert status_code == 403
            assert (register_response["success"] is False
                    and register_response["message"] == MESSAGE_REQUIRED_FIELD)

    @allure.title('Тест успешной авторизации зарегестрированного пользователя')
    def test_existing_user_login_success(self, reg_del_user):
        with allure.step('Подготовка тестовых данных и отправка запроса'):
            _, data_user = reg_del_user
            log_response, log_status_code = login_user(email=data_user['email'], password=data_user['password'])
        with allure.step('успешная авторизация пользователя'):
            assert log_status_code == 200 and log_response["success"] is True

    @allure.title('Тест авторизации с неверными данными для входа')
    def test_user_login_invalid_data_negative(self, reg_del_user):
        with allure.step('Подготовка тестовых данных и отправка запроса'):
            _, data_user = reg_del_user
            wrong_email = data_user['email'] + '123'
            wrong_password = data_user['password'] + '123FawdRRR'
            log_response, log_status_code = login_user(email=wrong_email, password=wrong_password)
        with allure.step('проверка невозможности авторизации'):
            assert log_status_code == 401
            assert log_response["success"] is False and log_response["message"] == MESSAGE_INCORRECT_LOGIN
