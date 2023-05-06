class Car():
    """Создаем автомобиль"""

    def __init__(self, model, year, engine_volume, price, mileage):
        """Инициализируем атрибуты автомобиля"""
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def car_description(self):
        """Получаем описание автомобиля"""
        description = self.model + ' ' + str(self.year) + ' года выпуска, объем двигателя ' + str(self.engine_volume) + ' куб. см, его стоимость ' + str(self.price) + ', пробег ' + str(self.mileage) + ' км, количество колес: ' + str(self.wheels)
        print('Новый автомобиль: ' + description)


class Truck(Car):
    """Создаем класс грузовика"""
    def __init__(self, model, year, engine_volume, price, mileage):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(model, year, engine_volume, price, mileage)
        self.wheels = 8



audi = Car('Audi', 2020, 2967, 5000000, 200)
audi.car_description()

auto_transport_truck = Truck('Mercedes-Benz', 2017, 7698, 10000000, 6000)
auto_transport_truck.car_description()
