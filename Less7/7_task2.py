# Дана строка, длина которой не превосходит 1000. 
# Вам требуется преобразовать все идущие подряд пробелы в один. 
# Выведите измененную строку.

str = 'aaa bbb  ccc   ddd     eee      fff       ggg'


# варинат а) дотех пор, пока есть 2 пробела, заменяем их на 1
"""
while str.count('  ')>0:
   str = str.replace('  ', ' ')
"""

# вариант б) собираем новую строку посимвольно: 
# если текущий и предыдущий символ пробелы - текущий игнорируем
c_prev = ''
res = ''
for c in str:
   # предыдущий символ не пробел
   if c != ' ':
      res += c
   # текущий символ пробел, но предыдущий не пробел
   elif (c == ' ') and (c_prev != ' '):
      res += c
   # сохраняем предыдущий
   c_prev = c

print(res)




