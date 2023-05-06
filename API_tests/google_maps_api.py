import requests

class Test_new_location():
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""

        base_url = 'https://rahulshettyacademy.com' # базовый url
        key = '?key=qaclick123' # параметр

        """Создание новой локации"""

        post_resource = '/maps/api/place/add/json'  # ручка

        post_url = base_url + post_resource + key
        print(post_url)
        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json = json_for_create_new_location)
        print(result_post.text)
        print('Статус код ' + str(result_post.status_code))
        assert 200 == result_post.status_code
        print("Успешно!!! Создана новая локация")
        check_post = result_post.json()
        check_info_post = check_post.get('status')
        print(f"Статус код ответа: {check_info_post}")
        assert check_info_post == 'OK'
        print('Статус ответа верен')

        place_id = check_post.get('place_id')
        print(f"Идентификатор локации: {place_id}")

        """Проверка создания новой локации"""

        get_resource = '/maps/api/place/get/json'
        get_url = base_url + get_resource + key + f'&place_id={place_id}'
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print(f"Статус код ответа: {result_get.status_code}")
        assert 200 == result_get.status_code
        print('Проверка создания новой локации прошла успешно')

        """Изменение новой локации"""

        put_resource = '/maps/api/place/update/json'
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_location_address = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json = json_for_update_location_address)
        print(result_put.text)
        print(f"Статус код ответа: {result_put.status_code}")
        assert 200 == result_put.status_code
        print('Изменение новой локации прошло успешно')
        check_put = result_put.json()
        check_put_info = check_put.get('msg')
        print(f"Ответ: {check_put_info}")
        assert check_put_info == 'Address successfully updated'
        print('Сообщение верно')

        """Проверка изменения адреса"""

        result_get = requests.get(get_url)
        print(result_get.text)
        print(f"Статус код ответа: {result_get.status_code}")
        assert 200 == result_get.status_code
        print('Проверка изменения адреса прошла успешно')
        check_address = result_get.json()
        check_address_info = check_address.get('address')
        print(f"Адрес: {check_address_info}")
        assert check_address_info == '100 Lenina street, RU'
        print('Адрес изменен')

        """Удаление новой локации"""

        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_location = {
            "place_id": place_id
        }
        result_delete = requests.delete(delete_url, json=json_for_delete_location)
        print(result_delete.text)
        print(f"Статус код ответа: {result_delete.status_code}")
        assert 200 == result_delete.status_code
        print('Удаление новой локации прошло успешно')
        check_delete = result_delete.json()
        check_delete_info = check_delete.get('status')
        print(f"Ответ: {check_delete_info}")
        assert check_delete_info == 'OK'
        print('Статус верен')

        """Проверка удаления адреса"""

        result_get = requests.get(get_url)
        print(result_get.text)
        print(f"Статус код ответа: {result_get.status_code}")
        assert 404 == result_get.status_code
        print('Проверка удаления адреса прошла успешно')
        check_msg = result_get.json()
        check_msg_info = check_msg.get('msg')
        print(f"Сообщение: {check_msg_info}")
        assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists"
        print('Удаление произведено верно')

        print('Тестирование Test_new_location завершено успешно')


new_place = Test_new_location()
new_place.test_create_new_location()
