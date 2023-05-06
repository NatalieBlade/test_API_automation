class Person():
    """Создаем человека"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100 # если передаем значение по дефолту, атрибут не указываем

    def description_person(self):
        """Получаем описание человека"""
        description = self.name + ', ему ' + str(self.age) + ' лет, его рост ' + str(self.height) + ' см, его вес ' + str(self.weight) + ' кг'
        print('Нового человека зовут ' + description)

    def get_weight(self):
        """Получаем вес человека"""
        print('Вес нашего человека ' + str(self.weight))

    def update_weight(self, kg):
        """Изменяем вес человека"""
        self.weight = kg


class Warrior(Person):
    """Создаем класс воина"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получаем заряд ярости"""
        print('Заряд ярости героя равен: ' + str(self.rage))

    def description_person(self):
        """Переопледеление метода родителя"""
        description = self.name + ', ему ' + str(self.age) + ' лет, его заряд ярости ' + str(self.rage)
        # print('Героя зовут ' + description)
        return description

