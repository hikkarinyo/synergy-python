# Погодные условия: облака и грозы

import random
from constants import EMPTY, CLOUD, THUNDER, TREE, FIRE


class Weather:
    def __init__(self):
        self.current = EMPTY     # текущая погода
        self.timer = 0           # сколько тиков осталось

    def update(self, field, width, height):
        """
        Обновляет погоду за один тик.
        Гроза может поджечь случайное дерево.
        """
        if self.timer > 0:
            self.timer -= 1
            if self.timer == 0:
                self.current = EMPTY
        elif random.random() < 0.03:
            self.current = random.choice([CLOUD, THUNDER])
            self.timer = random.randint(5, 15)

        # гроза поджигает дерево
        if self.current == THUNDER and random.random() < 0.3:
            self._lightning_strike(field, width, height)

    def _lightning_strike(self, field, width, height):
        """Поджигает случайное дерево молнией."""
        trees = [(x, y) for y in range(height)
                         for x in range(width)
                         if field[y][x] == TREE]
        if trees:
            x, y = random.choice(trees)
            field[y][x] = FIRE

    def description(self):
        """Возвращает строку с описанием погоды."""
        if self.current == EMPTY:
            return ""
        return f"Погода: {self.current}  (осталось тиков: {self.timer})"