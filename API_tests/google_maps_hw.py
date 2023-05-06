import requests

class Test_new_location():
    """Работа с новыми локациями"""

    def test_create_new_location(self):
        """Создание новой локации"""

        base_url = 'https://rahulshettyacademy.com'
        key = '?key=qaclick123'

        """Создание новых локаций"""

        post_resource = '/maps/api/place/add/json'

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
        with open('text.txt', 'a') as fa:
            fa.write(place_id + '\n')

        """Проверка создания новой локации"""

        get_resource = '/maps/api/place/get/json'
        with open('text.txt', 'r') as fr:
            place_ids = fr.readlines()
            print(place_ids)
        get_url = base_url + get_resource + key + '&place_id=' + place_ids[-1].rstrip("\n")
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print(f"Статус код ответа: {result_get.status_code}")
        assert 200 == result_get.status_code
        print('Проверка создания новой локации прошла успешно')

    def delete_new_location(self):
        """Удаление новых локаций"""

        base_url = 'https://rahulshettyacademy.com'
        key = '?key=qaclick123'
        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resource + key
        print(delete_url)
        with open('text.txt', 'r') as fr:
            place_ids = fr.readlines()
            print(place_ids)
        ids_needed = []
        for f in range(len(place_ids)):
            if f % 2 != 0:
                ids_needed.append(place_ids[f])
        print(ids_needed)
        for f in ids_needed:
            json_for_delete_location = {
                "place_id": f.rstrip("\n")
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

        """Проверка удаления локаций"""

        get_resource = '/maps/api/place/get/json'
        for f in ids_needed:
            get_url = base_url + get_resource + key + '&place_id=' + f.rstrip("\n")
            result_get = requests.get(get_url)
            print(result_get.text)
            print(f"Статус код ответа: {result_get.status_code}")
            assert 404 == result_get.status_code
            print('Проверка удаления адреса прошла успешно')
            check_msg = result_get.json()
            check_msg_info = check_msg.get('msg')
            print(f"Сообщение: {check_msg_info}")
            assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists"
            print('Удаление произведено корректно')


new_place = Test_new_location()
i = 0
while i < 5:
    new_place.test_create_new_location()
    i += 1
new_place.delete_new_location()
