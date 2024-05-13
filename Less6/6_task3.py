# Вводятся целые числа A и B. 
# Гарантируется, что A ≤ B. 
# Выведите все четные числа на заданном отрезке через пробел.

A = int(input())
B = int(input())
res = ""

for i in range(A, B + 1):
    if i % 2 == 0:
        if res == "":
            res = str(i)
        else:
            res += " " + str(i)

print(res)
 




