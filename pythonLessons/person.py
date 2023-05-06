# self - ссылка на класс и атрибуты класса

class Person():
    """Модель человека"""

    def __init__(self, name, age):
        """Инициализация атрибутов человека - имя, возраст"""
        self.name = name
        self.age = age
        print('Человек создан')

    def sing(self):
        """Просим человека  спеть"""
        print(self.name + ' поёт')

    def dance(self):
        """Просим человека  станцевать"""
        print(self.name + ' танцует')

# В переменной man хранится экземпляр класса Person c его атрибутами
man = Person('Egor', 39)
woman = Person('Anna', 30)
# print(man.name)

man.dance()
woman.sing()

