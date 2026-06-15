# Точка входа в игру. Запускает главный цикл.
from constants import DEFAULT_WIDTH, DEFAULT_HEIGHT
from game import Game


def main():
    print("🚁 ПОЖАРНЫЙ ВЕРТОЛЁТ")
    print("=" * 30)
    print("Тушите пожары, набирайте воду в реках,")
    print("посещайте госпиталь и магазин улучшений!")
    print()

    try:
        w = int(input(f"Ширина поля (по умолчанию {DEFAULT_WIDTH}): ") or DEFAULT_WIDTH)
        h = int(input(f"Высота поля (по умолчанию {DEFAULT_HEIGHT}): ") or DEFAULT_HEIGHT)
    except ValueError:
        w, h = DEFAULT_WIDTH, DEFAULT_HEIGHT

    game = Game(w, h)

    while True:
        game.render()

        if game.check_game_over():
            print(f"\nИГРА ОКОНЧЕНА! Итоговый счёт: {game.helicopter.score}")
            break

        cmd = input("Команда: ").strip().lower()

        if cmd == 'w':
            game.handle_move(0, -1)
        elif cmd == 's':
            game.handle_move(0, 1)
        elif cmd == 'a':
            game.handle_move(-1, 0)
        elif cmd == 'd':
            game.handle_move(1, 0)
        elif cmd == 'e':
            game.handle_extinguish()
        elif cmd == 'q':
            game.handle_collect_water()
        elif cmd == 'h':
            from shop import visit_hospital
            visit_hospital(game.helicopter)
        elif cmd == 'b':
            from shop import visit_shop
            visit_shop(game.helicopter)
        elif cmd == 'v':
            game.handle_save()
        elif cmd == 'l':
            game.handle_load()
        elif cmd == 'x':
            print("Пока!")
            break
        else:
            print("неизвестная команда")


if __name__ == "__main__":
    main()