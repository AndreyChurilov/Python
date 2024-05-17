# Вспомогательная Функция get_pet(ID, pets) - проверка наличия питомца по ID
# Вспомогательная Функция get_suffix(pet_age) - год/года/лет
# Функция create(pets) - добавление питомца
# Функция read(pets) - вывод данных о питомце
# Вспомогательная Функция read_item(ID, pets) - вывод данных о питомце по ID
# Вспомогательная pets_list(pets) - вывод данных о всех питомцах
# Функция update(pets)- изменение данных о питомце
# Функция delete(pets) - удаление данных о питомце

import collections

def get_pet(ID, pets):
    if ID in pets.keys():
        return True
    return False

def get_suffix(pet_age):
    year_case = ''
    if (pet_age % 10 == 1) and (pet_age != 11) and (pet_age % 100 != 11):
       year_case = 'год'
    elif (1 < pet_age % 10 <= 4) and (pet_age != 12) and (pet_age != 13) and (pet_age != 14):
       year_case = 'года'
    else:
       year_case = 'лет'
    return year_case

def create(pets):
    print('Имя нового питомца:')
    pet_name = input()
    print('Вид питомца:')
    pet_type = input()
    print('Возраст питомца:')
    pet_age = input()
    print('Имя владельца питомца:')
    pet_owner = input()

    tmp_item = dict()
    tmp_item["Вид питомца"] = pet_type
    tmp_item["Возраст питомца"] = pet_age
    tmp_item["Имя владельца"] = pet_owner

    tmp_pet = dict()
    tmp_pet[pet_name] = tmp_item

    if len(pets)>0:
        last = collections.deque(pets, maxlen=1)[0]
    else:
        last = 0
    ID = last + 1
    
    pets[ID] = tmp_pet
    print(f'Питомец добавлен с ID: {ID}')


def read(pets):
    print('Введите ID питомца:')
    ID = int(input())
    if get_pet(ID, pets):
        read_item(ID, pets)
    else:
        print(f'Питомец с ID={ID} не найден!')

def read_item(ID, pets):
    tmp_pet = pets[ID]
    for key, val in tmp_pet.items():
        pet_name = key
        pet_type = val["Вид питомца"] 
        pet_age  = int(val["Возраст питомца"])
        pet_owner = val["Имя владельца"]
        year_case = get_suffix(pet_age)    
        print(f'Это {pet_type} по кличке "{pet_name}". Возраст питомца: {pet_age} {year_case}. Имя владельца: {pet_owner}')

def pets_list(pets):   
    for key in pets.keys():
        read_item(key, pets)       

def update(pets):
    print('Введите ID питомца:')
    ID = int(input())
    if get_pet(ID, pets):
        tmp_pet = pets[ID]
        tmp_pet.clear()

        print('Имя питомца:')
        pet_name = input()
        print('Вид питомца:')
        pet_type = input()
        print('Возраст питомца:')
        pet_age = input()
        print('Имя владельца питомца:')
        pet_owner = input()

        tmp_item = dict()
        tmp_item["Вид питомца"] = pet_type
        tmp_item["Возраст питомца"] = pet_age
        tmp_item["Имя владельца"] = pet_owner

        tmp_pet = dict()
        tmp_pet[pet_name] = tmp_item
        
        pets[ID] = tmp_pet

        print(f'Данные по питомецу с ID: {ID} изменены')
    else:
        print(f'Питомец с ID={ID} не найден!')  

def delete(pets):
    print('Введите ID питомца:')
    ID = int(input())
    if get_pet(ID, pets):
        pets.pop(ID)
        print(f'Питомец ID: {ID} успешно удален')
    else:
        print(f'Питомец с ID={ID} не найден!')           

pets = dict()

command = ''
while command!= 'stop':
    print('ВВЕДИТЕ КОМАНДУ:')
    command = input()

    if command == 'create':
        create(pets)
    elif command == 'read':
        read(pets)        
    elif command == 'update':
        update(pets)   
    elif command == 'delete':
        delete(pets)   
    elif command == 'list': #вывести всех
        pets_list(pets)                
    elif command == 'stop':
        print('-----Выход-----')
    else:
        print('Команда не распознана!!!')

""" 
--- Для теста ---
Мухтар
Собака
9
Павел

Каа
Желторотый питон
19
Саша
"""


