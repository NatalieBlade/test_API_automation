import requests

class Test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        """Создание случайной шутки"""

        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        assert 200 == result.status_code
        print("Успешно!!! Мы получили новую шутку")
        result.encoding = 'utf-8'
        print('Статус код ' + str(result.status_code))
        print(result.text)
        check = result.json()

        check_info = check.get("categories")
        print(check_info)
        assert check_info == []
        print('Категория верна!')

        check_value = check.get("value")
        print(check_value)
        name = 'Chuck'
        if name in check_value:
            print('Chuck присутствует в шутке')
        else:
            print('Chuck отсутствует в шутке')

    def test_create_new_random_category_joke(self):
        """Создание случайной шутки на определенную тему"""

        category = 'sport'
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print('Статус код ' + str(result.status_code))
        assert 200 == result.status_code
        print("Успешно!!! Мы получили шутку на тему 'спорт'")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()

        check_info = check.get("categories")
        print(check_info)
        assert check_info == ['sport']
        print('Категория верна!')

        check_value = check.get("value")
        print(check_value)
        name = 'Chuck'
        if name in check_value:
            print('Chuck присутствует в шутке')
        else:
            print('Chuck отсутствует в шутке')


# random_joke = Test_new_joke()
# random_joke.test_create_new_random_joke()

category_joke = Test_new_joke()
category_joke.test_create_new_random_category_joke()


