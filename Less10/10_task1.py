# Создать словарь со словарем внутри
# pets = {
# "Имя питомца": {
#   'Вид питомца': # придумайте каким образом сюда внести информацию,
#   'Возраст питомца': # придумайте каким образом сюда внести информацию,
#   'Имя владельца': # придумайте каким образом сюда внести информацию
#  }
# }
# Вывести информацию используя методы keys() и values()
# Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша

# 1) заполнить словарь
pets = dict()

while (True):
    print('Имя питомца (Enter для выхода):')
    pet_name = input()
    if pet_name == '':
        break
    else:
        print('Вид питомца:')
        pet_type = input()
        print('Возраст питомца:')
        pet_age = input()
        print('Имя владельца питомца:')
        pet_owner = input()

        tmp = dict()
        tmp["Вид питомца"] = pet_type
        tmp["Возраст питомца"] = pet_age
        tmp["Имя владельца"] = pet_owner

        pets[pet_name] = tmp

# 2) вывести данные из словаря
for key, val in pets.items():
   pet_name = key
   pet_type = val["Вид питомца"] 
   pet_age  = int(val["Возраст питомца"])
   pet_owner = val["Имя владельца"]
   year_case = ''
   if (pet_age % 10 == 1) and (pet_age != 11) and (pet_age % 100 != 11):
       year_case = 'год'
   elif (1 < pet_age % 10 <= 4) and (pet_age != 12) and (pet_age != 13) and (pet_age != 14):
       year_case = 'года'
   else:
       year_case = 'лет'

   print(f'Это {pet_type} по кличке "{pet_name}". Возраст питомца: {pet_age} {year_case}. Имя владельца: {pet_owner}')





