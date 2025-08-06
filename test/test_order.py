import allure
from methods.request import create_order
from data.data import INGREDIENTS, BAD_INGREDIENTS, MESSAGE_NOT_INGREDIENT, MESSAGE_NOT_AUTH


@allure.epic('Класс тестирования заказов')
class TestOrder:

    @allure.title('Тест успешного заказа авторизованным пользователем')
    def test_order_with_auth_success(self, reg_log_del_user):
        with allure.step('Подготовка тестовых данных и отправка запроса'):
            token = reg_log_del_user
            expected_keys_response = ["name", "order", "success"]
            response, status_code = create_order(ingredients=INGREDIENTS, token=token)
            response = response.json()
            actual_keys_response = list(response.keys())
        with allure.step('Проверка успешного создания заказа'):
            assert status_code == 200
            assert set(expected_keys_response) == set(actual_keys_response)

    @allure.title('Тестирование невозможности создания заказа неавторизованным пользователем')
    def test_order_without_auth_negative(self):
        with allure.step('отправка запроса'):
            response, status_code = create_order(ingredients=INGREDIENTS, token=None)
        with (allure.step('Проверка невозможности создания заказа')):
            assert status_code == 401 and (response.json()).get("message") == MESSAGE_NOT_AUTH

    @allure.title('Тестирование невозможности создания заказа с невалидными данными')
    def test_order_with_bad_ingredient_negative(self, reg_log_del_user):
        with allure.step('Подготовка тестовых данных и отправка запроса'):
            token = reg_log_del_user
            _, status_code = create_order(ingredients=BAD_INGREDIENTS, token=token)
        with allure.step('Проверка невозможности создания заказа с невалидными данными'):
            # нет тело ответа сервера, возвращает только статус код
            assert status_code == 500

    @allure.title('Тестирование невозможности создания заказа без ингридиентов')
    def test_order_without_ingredient_negative(self, reg_log_del_user):
        with allure.step('Подготовка тестовых данных и отправка запроса'):
            token = reg_log_del_user
            response, status_code = create_order(ingredients=None, token=token)
        with allure.step('Проверка невозможности создания заказа с невалидными данными'):
            response = response.json()
            assert status_code == 400 and response["message"] == MESSAGE_NOT_INGREDIENT
