# Создайте функцию, которая принимает в качестве параметра - натуральное целое число.
# Данная функция находит факториал полученного числа
# Теперь создайте список факториалов чисел от получившегося ранее факториала 6, до 1.

def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res


print('Введите целое число:')
x = int(input())

lst = []
n_from = fact(x)
n_to = 1

for i in range(n_from,n_to-1,-1):
    val = fact(i)
    lst.append(val)

print(lst)


