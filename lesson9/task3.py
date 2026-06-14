# Задание №3
# Во входную строку вводится последовательность чисел через пробел.
# Для каждого числа выведите "YES", если это число ранее встречалось
# в последовательности, или "NO" если не встречалось.

nums = list(map(int, input().split()))
seen = set()

for num in nums:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)
        