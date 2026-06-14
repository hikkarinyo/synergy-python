# Задание №2
# В Урок №10. Задание №1 вы создавали словарь с информацией о питомце.
# Теперь нам нужна "настоящая" база данных для ветеринарной клиники.
# Создайте функции create, read, update, delete.
# Программа работает в цикле while, пока пользователь не введёт 'stop'.
# Функция create добавляет новую запись, увеличивая идентификатор на единицу.
# Функция read отображает информацию о питомце.
# Функция update обновляет информацию об указанном питомце.
# Функция delete удаляет запись о питомце.

import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
}


def get_pet(ID):
    # функция получает информацию о питомце по ID
    # если питомца с таким ID нет - возвращает False
    return pets[ID] if ID in pets.keys() else False


def get_suffix(age):
    # функция возвращает правильное склонение: год, года, лет
    if 11 <= age % 100 <= 19:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"


def pets_list():
    # выводит список всех питомцев
    for ID, pet_data in pets.items():
        for name, info in pet_data.items():
            suffix = get_suffix(info["Возраст питомца"])
            print(f'[{ID}] Это {info["Вид питомца"]} по кличке "{name}". '
                  f'Возраст питомца: {info["Возраст питомца"]} {suffix}. '
                  f'Имя владельца: {info["Имя владельца"]}')


def create():
    # добавляет новую запись в базу данных
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1

    name = input("Кличка питомца: ")
    species = input("Вид питомца: ")
    age = int(input("Возраст питомца: "))
    owner = input("Имя владельца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": species,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Питомец добавлен с ID: {new_id}")


def read():
    # отображает информацию о питомце по ID
    ID = int(input("Введите ID питомца: "))
    pet_data = get_pet(ID)

    if not pet_data:
        print("Питомец с таким ID не найден")
        return

    for name, info in pet_data.items():
        suffix = get_suffix(info["Возраст питомца"])
        print(f'Это {info["Вид питомца"]} по кличке "{name}". '
              f'Возраст питомца: {info["Возраст питомца"]} {suffix}. '
              f'Имя владельца: {info["Имя владельца"]}')


def update():
    # обновляет информацию об указанном питомце
    ID = int(input("Введите ID питомца: "))
    pet_data = get_pet(ID)

    if not pet_data:
        print("Питомец с таким ID не найден")
        return

    for name, info in pet_data.items():
        print(f"Редактируем питомца: {name}")
        species = input(f'Вид питомца [{info["Вид питомца"]}]: ') or info["Вид питомца"]
        age = input(f'Возраст [{info["Возраст питомца"]}]: ')
        age = int(age) if age else info["Возраст питомца"]
        owner = input(f'Имя владельца [{info["Имя владельца"]}]: ') or info["Имя владельца"]

        pets[ID][name] = {
            "Вид питомца": species,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    print("Информация обновлена")


def delete():
    # удаляет запись о питомце по ID
    ID = int(input("Введите ID питомца: "))
    pet_data = get_pet(ID)

    if not pet_data:
        print("Питомец с таким ID не найден")
        return

    del pets[ID]
    print(f"Питомец с ID {ID} удалён")


# основной цикл программы
command = ""
while command != "stop":
    command = input("\nВведите команду (create / read / update / delete / list / stop): ")

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command != "stop":
        print("Неизвестная команда")
        