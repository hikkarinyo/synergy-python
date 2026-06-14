# Задание №2
# Создайте класс Autobus, который наследуется от класса Transport.
# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
# Используйте переопределение метода.
# Ожидаемый результат вывода:
# Вместимость одного автобуса Renaul Logan: 50 пассажиров

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

class Autobus(Transport):
    # переопределяем метод родителя со значением по умолчанию 50
    def seating_capacity(self, capacity=50):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

bus = Autobus("Renaul Logan", 180, 12)
print(bus.seating_capacity())
