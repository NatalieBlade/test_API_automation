import requests

class Test_user_category_joke():
    """Получение шутки по категори от пользователя"""

    def __init__(self):
        pass

    def test_get_user_category(self):
        """Получение категории от пользователя"""

        category = input('Введите желаемую категорию: ')
        print(category)
        return category

    def test_get_joke_categories(self):
        """Получение доступных категорий шуток"""

        url = "https://api.chucknorris.io/jokes/categories"
        print(url)
        result = requests.get(url)
        assert 200 == result.status_code
        print("Категрии успешно получены")
        result.encoding = 'utf-8'
        print('Статус код ' + str(result.status_code))
        print(result.text)
        return result.json()

    def test_joke_for_user_category(self, categories, category):
        """Получение случайной шутки на тему, выбранную пользователем"""

        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        if category in categories:
            print(f'Успешно!!! Мы получили шутку на тему {category}')
        else:
            print(f'Категория {category} недоступна')
        print('Статус код ' + str(result.status_code))
        assert 200 == result.status_code
        result.encoding = 'utf-8'
        print(result.text)


user_joke = Test_user_category_joke()
all_categories = user_joke.test_get_joke_categories()
user_category = user_joke.test_get_user_category()
user_joke.test_joke_for_user_category(all_categories, user_category)
