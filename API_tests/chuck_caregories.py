import requests

class Test_category_joke():
    """Получение шутки по категориям"""

    def __init__(self):
        pass

    def test_get_joke_categories(self):
        """Получение категорий шуток"""

        url = "https://api.chucknorris.io/jokes/categories"
        print(url)
        result = requests.get(url)
        assert 200 == result.status_code
        print("Категрии успешно получены")
        result.encoding = 'utf-8'
        print('Статус код ' + str(result.status_code))
        print(result.text)
        return result.json()

    def test_joke_for_each_category(self, category):
        """Получение случайной шутки на определенную тему"""

        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print('Статус код ' + str(result.status_code))
        assert 200 == result.status_code
        print("Успешно!!! Мы получили шутку на тему " + category)
        result.encoding = 'utf-8'
        print(result.text)


jokes = Test_category_joke()
categories_for_jokes = jokes.test_get_joke_categories()
for f in categories_for_jokes:
    jokes.test_joke_for_each_category(str(f))
