"""Методы для проверки ответов наших запросов"""
import json
from requests import Response

class Checking():

    """Метод для проверки статус кода"""
    @staticmethod
    def status_code_checking(response, status_code):
        assert status_code == response.status_code
        print(f'Успешно! Статус код = {str(response.status_code)}')

    """Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'Значение поля {field_name} верно!!!')

    """Метод для проверки значений обязательных полей в ответе запроса по заданному слову"""
    @staticmethod
    def check_json_search_word_in_value(response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f'Слово {search_word} присутствует!!!')
