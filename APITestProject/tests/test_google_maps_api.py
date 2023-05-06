from utils.api import Google_maps_api
import allure
from utils.check import Checking

# python -m pytest -s -v
# pip3 install pytest

# pip3 install allure-pytest
# python -m pytest --alluredir test_results/ tests/test_google_maps_api.py
# allure serve test_results/

# Получаем все поля ответа
# token = json.loads(result_delete.text)
# print(list(token))

"""Создание, изменение и удаление новой локации"""
@allure.epic('Test creates location')
class Test_create_place():

    @allure.description('Test creates, updates and delete location')
    def test_create_new_place(self):
        print('Метод POST')
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.status_code_checking(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print('Метод GET for POST')
        result_get = Google_maps_api.check_new_place(place_id)
        Checking.status_code_checking(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print('Метод PUT')
        result_put = Google_maps_api.change_new_place(place_id)
        Checking.status_code_checking(result_put, 200)
        Checking.check_json_token(result_put, ["msg"])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print('Метод GET for PUT')
        result_get = Google_maps_api.check_new_place(place_id)
        Checking.status_code_checking(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print('Метод DELETE')
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.status_code_checking(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print('Метод GET for DELETE')
        result_get = Google_maps_api.check_new_place(place_id)
        Checking.status_code_checking(result_get, 404)
        Checking.check_json_token(result_get, ["msg"])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')

        print('Тестирование создания, изменения и удаления новой локации прошло успешно')
