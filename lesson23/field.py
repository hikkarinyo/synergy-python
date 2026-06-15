# Генерация игрового поля: реки, деревья, госпиталь, магазин

import random
from constants import EMPTY, TREE, RIVER, HOSPITAL, SHOP


def create_empty_field(width, height):
    """Создаёт пустое поле заданного размера."""
    return [[EMPTY] * width for _ in range(height)]


def in_bounds(x, y, width, height):
    """Проверяет, принадлежит ли клетка с координатами полю."""
    return 0 <= x < width and 0 <= y < height


def find_empty(field, width, height):
    """Возвращает координаты случайной пустой клетки."""
    while True:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if field[y][x] == EMPTY:
            return x, y


def place_rivers(field, width, height):
    """Генерирует реки — случайные вертикальные полосы."""
    num_rivers = max(1, width // 6)
    for _ in range(num_rivers):
        x = random.randint(1, width - 2)
        for y in range(height):
            if random.random() < 0.7:
                field[y][x] = RIVER


def place_trees(field, width, height):
    """Генерирует деревья на пустых клетках."""
    for y in range(height):
        for x in range(width):
            if field[y][x] == EMPTY and random.random() < 0.35:
                field[y][x] = TREE


def place_hospital(field, width, height):
    """Размещает госпиталь на случайной пустой клетке."""
    x, y = find_empty(field, width, height)
    field[y][x] = HOSPITAL


def place_shop(field, width, height):
    """Размещает магазин улучшений на случайной пустой клетке."""
    x, y = find_empty(field, width, height)
    field[y][x] = SHOP


def generate_field(width, height):
    """Генерирует полное игровое поле."""
    field = create_empty_field(width, height)
    place_rivers(field, width, height)
    place_trees(field, width, height)
    place_hospital(field, width, height)
    place_shop(field, width, height)
    return field