# В первой строке вводится число N. 
# Далее в N строк вводится N чисел (1 ≤ N ≤ 10000), по одному числу на строке. 
# Все числа по модулю не превышают 10e5. 
# Переверните массив чисел. 
# Выведите N чисел - перевернутый массив.

N = int(input())
res = []
for i in range(N):
    res.append( int(input()) )

res.reverse()

print(res)



