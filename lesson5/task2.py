# Задание №2
# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв?
# Гласными называют буквы «a», «e», «i», «o», «u».
# Для решения задачи создайте переменную и в неё положите слово с помощью input()
# А также определите количество каждой из этих гласных букв
# Если какой-то из перечисленных букв нет - Выведите False

word = input("Введите слово: ")

vowels = "aeiou"

for v in vowels:
    count = word.count(v)
    if count > 0:
        print(f"{v}: {count}")
    else:
        print(False)

consonants = sum(1 for c in word if c not in vowels)
print(f"Согласных: {consonants}")
