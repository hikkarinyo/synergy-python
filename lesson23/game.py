# Основной класс Game: логика тиков, пожаров, отрисовки
import os
import random

from constants import EMPTY, TREE, FIRE, BURNT, RIVER, HELICOPTER, HOSPITAL, SHOP, THUNDER
from field import generate_field, find_empty, in_bounds
from helicopter import Helicopter
from weather import Weather
from shop import visit_hospital, visit_shop
from save import save_game, load_game


class Game:
    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.ticks  = 0

        # генерируем поле
        self.field = generate_field(width, height)

        # создаём вертолёт на пустой клетке
        hx, hy = find_empty(self.field, width, height)
        self.helicopter = Helicopter(hx, hy)

        # погода
        self.weather = Weather()

    # ─── Отрисовка ──────────────────────────────────────────────

    def render(self):
        """Выводит текущее состояние игры в консоль."""
        os.system('cls' if os.name == 'nt' else 'clear')

        h = self.helicopter
        print("=" * (self.width * 2 + 4))
        print(f"  🚁 ПОЖАРНЫЙ ВЕРТОЛЁТ  |  Тик: {self.ticks}")
        print(f"  ❤️  Жизни: {h.lives}  |  💧 Вода: {h.water}/{h.max_water}  |  ⭐ Очки: {h.score}")

        weather_desc = self.weather.description()
        if weather_desc:
            print(f"  {weather_desc}")

        print("=" * (self.width * 2 + 4))

        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if x == self.helicopter.x and y == self.helicopter.y:
                    row += HELICOPTER + " "
                else:
                    row += self.field[y][x] + " "
            print(" " + row)

        print("=" * (self.width * 2 + 4))
        print("w/a/s/d — движение  |  e — тушить  |  q — набрать воду")
        print("h — госпиталь  |  b — магазин  |  v — сохранить  |  l — загрузить  |  x — выход")

    # ─── Тик ────────────────────────────────────────────────────

    def tick(self):
        """Один игровой тик: рост деревьев, пожары, погода."""
        self.ticks += 1

        # случайный рост дерева
        if random.random() < 0.15:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.field[y][x] == EMPTY:
                self.field[y][x] = TREE

        # случайное возгорание
        if random.random() < 0.08:
            self._start_fire()

        # распространение пожара
        self._spread_fire()

        # погода
        self.weather.update(self.field, self.width, self.height)

    def _start_fire(self):
        """Поджигает случайное дерево."""
        trees = [(x, y) for y in range(self.height)
                         for x in range(self.width)
                         if self.field[y][x] == TREE]
        if trees:
            x, y = random.choice(trees)
            self.field[y][x] = FIRE

    def _spread_fire(self):
        """Пожар распространяется на соседние деревья и догорает."""
        new_field = [row[:] for row in self.field]
        for y in range(self.height):
            for x in range(self.width):
                if self.field[y][x] == FIRE:
                    # клетка догорает
                    if random.random() < 0.25:
                        new_field[y][x] = BURNT
                        self.helicopter.score -= 5
                    # распространение на соседей
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if in_bounds(nx, ny, self.width, self.height):
                            if self.field[ny][nx] == TREE and random.random() < 0.15:
                                new_field[ny][nx] = FIRE
        self.field = new_field

    # ─── Команды ────────────────────────────────────────────────

    def handle_move(self, dx, dy):
        """Обрабатывает движение вертолёта."""
        msg = self.helicopter.move(dx, dy, self.field, self.width, self.height)
        if msg:
            print(msg)
            return

        # проверяем клетку под вертолётом после перемещения
        cell = self.field[self.helicopter.y][self.helicopter.x]
        if cell == HOSPITAL:
            visit_hospital(self.helicopter)
        elif cell == SHOP:
            visit_shop(self.helicopter)

        self.tick()

    def handle_extinguish(self):
        """Обрабатывает команду тушения."""
        print(self.helicopter.extinguish(self.field))
        self.tick()

    def handle_collect_water(self):
        """Обрабатывает команду набора воды."""
        print(self.helicopter.collect_water(self.field))
        self.tick()

    def handle_save(self):
        save_game(self)
        input("Нажмите Enter...")

    def handle_load(self):
        load_game(self)
        input("Нажмите Enter...")

    # ─── Конец игры ─────────────────────────────────────────────

    def check_game_over(self):
        """Проверяет условие конца игры. Возвращает True если игра окончена."""
        damaged = self.helicopter.check_fire_damage(self.field)
        if damaged:
            print(f"Вертолёт попал в огонь! Жизни: {self.helicopter.lives}")
        return self.helicopter.is_dead()