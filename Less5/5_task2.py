# Дано слово из маленьких латинских букв. 
# Сколько там согласных и гласных букв? 
# Гласными называют буквы «a», «e», «i», «o», «u».
# Для решения задачи создайте переменную и в неё положите слово с помощью input()
# А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False

print("Введите слово из не более 5 маленьких латинских букв:")
word = input()

a_symb = 0
e_symb = 0
i_symb = 0
o_symb = 0
u_symb = 0

i = 1 # 1 буква
if (len(word) >= i):
   if word[i - 1] == "a":
      a_symb += 1
   if word[i - 1] == "e":
      e_symb += 1  
   if word[i - 1] == "i":
      i_symb += 1        
   if word[i - 1] == "o":
      o_symb += 1 
   if word[i - 1] == "u":
      u_symb += 1  

i = 2 # 2 буква
if (len(word) >= i):
   if word[i - 1] == "a":
      a_symb += 1
   if word[i - 1] == "e":
      e_symb += 1  
   if word[i - 1] == "i":
      i_symb += 1        
   if word[i - 1] == "o":
      o_symb += 1 
   if word[i - 1] == "u":
      u_symb += 1        

i = 3 # 3 буква
if (len(word) >= i):
   if word[i - 1] == "a":
      a_symb += 1
   if word[i - 1] == "e":
      e_symb += 1  
   if word[i - 1] == "i":
      i_symb += 1        
   if word[i - 1] == "o":
      o_symb += 1 
   if word[i - 1] == "u":
      u_symb += 1   

i = 4 # 4 буква
if (len(word) >= i):
   if word[i - 1] == "a":
      a_symb += 1
   if word[i - 1] == "e":
      e_symb += 1  
   if word[i - 1] == "i":
      i_symb += 1        
   if word[i - 1] == "o":
      o_symb += 1 
   if word[i - 1] == "u":
      u_symb += 1     

i = 5 # 5 буква
if (len(word) >= i):
   if word[i - 1] == "a":
      a_symb += 1
   if word[i - 1] == "e":
      e_symb += 1  
   if word[i - 1] == "i":
      i_symb += 1        
   if word[i - 1] == "o":
      o_symb += 1 
   if word[i - 1] == "u":
      u_symb += 1                              

vowels = a_symb + e_symb + i_symb + o_symb + u_symb
consonants = len(word) - vowels

print("Гласных: ", vowels, " Согласных:", consonants)

if (a_symb > 0):
   print("a: ", a_symb) 
else:
   print("a: ", False)   

if (e_symb > 0):
   print("e: ", e_symb) 
else:
   print("e: ", False)    

if (i_symb > 0):
   print("i: ", i_symb) 
else:
   print("i: ", False)   

if (o_symb > 0):
   print("o: ", o_symb) 
else:
   print("o: ", False)

if (u_symb > 0):
   print("u: ", u_symb) 
else:
   print("u: ", False)        
 




