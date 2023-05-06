import requests

class Test_star_wars_cast():
    """Работа с персонажами фильмов Звёздные войны"""

    def test_get_star_wars_cast(self):
        """Получение персонажей, снимавшихся в фильмах с Дарт Вейдером"""

        base_url = 'https://swapi.dev'

        """Получение фильмов, в которых снимался Дарт Вейдер"""
        get_resource = '/api/people/4/'
        get_url = base_url + get_resource
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print('Статус код ' + str(result_get.status_code))
        assert 200 == result_get.status_code
        print("Успешно!!! Фильмы получены")
        check_get = result_get.json()
        dart_weider_films = check_get.get('films')
        print(f"Фильмы с участием Дарта Вейдера: {dart_weider_films}")

        characters = set()
        for f in dart_weider_films:
            """Получение персонажей для каждого фильма с Дарт Вейдером"""
            get_url = f
            result_get = requests.get(get_url)
            print(result_get.text)
            print('Статус код ' + str(result_get.status_code))
            assert 200 == result_get.status_code
            print("Успешно!!! Информация о фильме получена")
            check_get = result_get.json()
            film_characters = check_get.get('characters')
            print(f"Герои фильма {f}: {film_characters}")
            for s in film_characters:
                """Получение имен персонажей из каждого фильма с Дарт Вейдером"""
                get_url = s
                result_get = requests.get(get_url)
                print(result_get.text)
                print('Статус код ' + str(result_get.status_code))
                assert 200 == result_get.status_code
                print("Успешно!!! Данные персонажа получены")
                check_get = result_get.json()
                character_name = check_get.get('name')
                print(f"Имя персонажа из фильма {f}: {character_name}")
                characters.add(character_name)
                print(characters)
        with open('dart_weider_films_cast.txt', 'a', encoding='utf-8') as fa:
            for f in characters:
                fa.write(f + '\n')


new_place = Test_star_wars_cast()
new_place.test_get_star_wars_cast()
