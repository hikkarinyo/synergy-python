# Задание №3
# Вводятся целые числа A и B. Гарантируется, что A ≤ B.
# Выведите все четные числа на заданном отрезке через пробел.

a = int(input())
b = int(input())

evens = [str(n) for n in range(a, b + 1) if n % 2 == 0]
print(*evens)
