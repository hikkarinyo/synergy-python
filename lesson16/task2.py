# Задание №2
# Создайте класс Черепашка, который хранит позиции x и y черепашки,
# а также s - количество клеточек, на которое она перемещается за ход.
# Методы:
# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает x на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать <= 0
# count_moves(x2, y2) - возвращает минимальное количество действий,
# за которое черепашка сможет добраться до x2 y2 от текущей позиции

import math

class Черепашка:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s
        print(f"Позиция: ({self.x}, {self.y})")

    def go_down(self):
        self.y -= self.s
        print(f"Позиция: ({self.x}, {self.y})")

    def go_left(self):
        self.x -= self.s
        print(f"Позиция: ({self.x}, {self.y})")

    def go_right(self):
        self.x += self.s
        print(f"Позиция: ({self.x}, {self.y})")

    def evolve(self):
        self.s += 1
        print(f"Шаг увеличен до: {self.s}")

    def degrade(self):
        if self.s - 1 <= 0:
            raise ValueError(f"Нельзя уменьшить шаг — s станет <= 0")
        self.s -= 1
        print(f"Шаг уменьшен до: {self.s}")

    def count_moves(self, x2, y2):
        # минимальное количество ходов = максимум из расстояний по x и y,
        # делённых на s (округляем вверх)
        dx = math.ceil(abs(x2 - self.x) / self.s)
        dy = math.ceil(abs(y2 - self.y) / self.s)
        moves = max(dx, dy)
        print(f"Минимум ходов до ({x2}, {y2}): {moves}")
        return moves


# пример использования
turtle = Черепашка(0, 0, 2)
turtle.go_up()
turtle.go_right()
turtle.evolve()
turtle.count_moves(10, 6)
turtle.degrade()
