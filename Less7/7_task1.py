# На вход подается 1 строка без пробелов. 
# По данной строке определите, является ли она палиндромом 
# (то есть, можно ли прочесть ее наоборот, как, например, слово "шалаш"). 
# Необходимо вывести ”yes”, если строка является палиндромом, и “no” в противном случае.

str = input()
str_part1 = str[0: len(str)//2 ]
if len(str) % 2 == 0:
    str_part2 = str[len(str) - 1: len(str)//2 - 1: -1]
else:
    str_part2 = str[len(str) - 1: len(str)//2: -1]

if str_part1.upper() == str_part2.upper():
    print("yes")
else:
    print("no")
 




