# Вводится натуральное число X. 
# Подсчитайте количество натуральных делителей числа X (включая 1 и само число). 
# x ≤ 2e9 (2 миллиарда)

x = int(input())
y = 1
cnt = 0

while y <= x:
    if x % y == 0:
        cnt += 1
    y += 1

print("Количество натуральных делителей:", cnt)
 



