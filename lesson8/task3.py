# Задание №3
# На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег.
# Одна лодка может выдержать не более m килограмм, при этом в лодку помещается не более 2 человек.
# Определите, какое минимальное число лодок нужно, чтобы перевезти на другой берег всех рыбаков.

m = int(input())
n = int(input())
weights = [int(input()) for _ in range(n)]

weights.sort()
left = 0
right = n - 1
boats = 0

while left <= right:
    if left == right:  # остался один рыбак
        boats += 1
        break
    if weights[left] + weights[right] <= m:  # лёгкий и тяжёлый влезают вместе
        left += 1
    right -= 1
    boats += 1

print(boats)
