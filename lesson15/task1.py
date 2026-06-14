# Задание №1
# Есть родительский класс Transport.
# Создайте объект Autobus, который унаследует все переменные и методы
# родительского класса Transport и выведете его.
# Ожидаемый результат вывода:
# Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    pass

bus = Autobus("Renaul Logan", 180, 12)
print(f"Название автомобиля: {bus.name} Скорость: {bus.max_speed} Пробег: {bus.mileage}")
