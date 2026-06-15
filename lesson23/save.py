# Сохранение и восстановление игры из файла

import json
import os

SAVE_FILE = "save.json"


def save_game(game, filename=SAVE_FILE):
    """Сохраняет текущее состояние игры в JSON-файл."""
    data = {
        "width":         game.width,
        "height":        game.height,
        "field":         game.field,
        "hx":            game.helicopter.x,
        "hy":            game.helicopter.y,
        "water":         game.helicopter.water,
        "max_water":     game.helicopter.max_water,
        "lives":         game.helicopter.lives,
        "score":         game.helicopter.score,
        "ticks":         game.ticks,
        "weather":       game.weather.current,
        "weather_timer": game.weather.timer,
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Игра сохранена в {filename}")


def load_game(game, filename=SAVE_FILE):
    """Загружает состояние игры из JSON-файла."""
    if not os.path.exists(filename):
        print("Файл сохранения не найден.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    game.width               = data["width"]
    game.height              = data["height"]
    game.field               = data["field"]
    game.helicopter.x        = data["hx"]
    game.helicopter.y        = data["hy"]
    game.helicopter.water    = data["water"]
    game.helicopter.max_water = data["max_water"]
    game.helicopter.lives    = data["lives"]
    game.helicopter.score    = data["score"]
    game.ticks               = data["ticks"]
    game.weather.current     = data["weather"]
    game.weather.timer       = data["weather_timer"]

    print("Игра загружена!")