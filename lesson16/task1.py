# Задание №1
# Создайте класс Касса, который хранит текущее количество денег в кассе.
# Методы:
# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

class Касса:
    def __init__(self, amount=0):
        self.amount = amount

    def top_up(self, x):
        self.amount += x
        print(f"Пополнено на {x}. Итого в кассе: {self.amount}")

    def count_1000(self):
        print(f"Целых тысяч в кассе: {self.amount // 1000}")

    def take_away(self, x):
        if x > self.amount:
            raise ValueError(f"Недостаточно денег. В кассе: {self.amount}, запрошено: {x}")
        self.amount -= x
        print(f"Забрано {x}. Остаток в кассе: {self.amount}")


# пример использования
kassa = Касса(5500)
kassa.top_up(1500)
kassa.count_1000()
kassa.take_away(2000)
