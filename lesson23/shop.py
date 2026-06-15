# Госпиталь и магазин улучшений

def visit_hospital(helicopter):
    """
    Госпиталь: восстанавливает 1 жизнь за 20 очков.
    Возвращает сообщение о результате.
    """
    print("\n🏥 ГОСПИТАЛЬ")
    if helicopter.lives >= 5:
        print("У вас максимум жизней (5).")
    elif helicopter.score >= 20:
        helicopter.score -= 20
        helicopter.lives += 1
        print(f"❤️  +1 жизнь за 20 очков. Жизни: {helicopter.lives}, Очки: {helicopter.score}")
    else:
        print(f"❌ Недостаточно очков (нужно 20, у вас {helicopter.score}).")
    input("Нажмите Enter...")


def visit_shop(helicopter):
    """
    Магазин: увеличивает резервуар воды за 30 очков.
    """
    print("\nМАГАЗИН УЛУЧШЕНИЙ")
    print(f"Текущий резервуар: {helicopter.max_water}")
    print(f"Улучшение резервуара: 30 очков (у вас {helicopter.score})")
    choice = input("Купить улучшение? (y/n): ").strip().lower()
    if choice == 'y':
        if helicopter.score >= 30:
            helicopter.score -= 30
            helicopter.max_water += 1
            print(f"Резервуар увеличен до {helicopter.max_water}!")
        else:
            print("Недостаточно очков.")
    input("Нажмите Enter...")