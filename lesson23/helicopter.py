# Класс Helicopter: позиция, вода, жизни, движение, тушение

from constants import RIVER, FIRE, TREE, BURNT


class Helicopter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.water = 0       # текущий запас воды
        self.max_water = 1   # максимум резервуаров
        self.lives = 3       # жизни
        self.score = 0       # очки

    def move(self, dx, dy, field, width, height):
        """
        Перемещает вертолёт на dx, dy.
        Возвращает сообщение о результате.
        """
        nx, ny = self.x + dx, self.y + dy

        if not (0 <= nx < width and 0 <= ny < height):
            return "Край карты!"

        cell = field[ny][nx]

        # набор воды при полёте над рекой
        if cell == RIVER and self.water < self.max_water:
            self.water += 1

        self.x, self.y = nx, ny
        return None

    def extinguish(self, field):
        """
        Тушит пожар на текущей клетке.
        Возвращает сообщение о результате.
        """
        cell = field[self.y][self.x]
        if cell == FIRE:
            if self.water > 0:
                field[self.y][self.x] = TREE
                self.water -= 1
                self.score += 10
                return "Пожар потушен! +10 очков"
            else:
                return "Нет воды! Летите к реке"
        return "Здесь нет пожара."

    def collect_water(self, field):
        """
        Набирает воду если вертолёт над рекой.
        Возвращает сообщение о результате.
        """
        if field[self.y][self.x] == RIVER:
            if self.water < self.max_water:
                self.water = self.max_water
                return f"Резервуар заполнен! ({self.water}/{self.max_water})"
            return "Резервуар уже полон."
        return "Здесь нет воды. Летите к реке"

    def check_fire_damage(self, field):
        """
        Проверяет, стоит ли вертолёт на огне — если да, теряет жизнь.
        Возвращает True если жизни кончились.
        """
        if field[self.y][self.x] == FIRE:
            self.lives -= 1
            field[self.y][self.x] = BURNT
            return True
        return False

    def is_dead(self):
        """Возвращает True если жизней не осталось."""
        return self.lives <= 0