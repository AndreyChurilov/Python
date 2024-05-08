# А теперь мы с тобой напишем форму ввода ответа на тест по биологии для студентов.
# Он должен запрашивать по порядку этапы развития человека
# и в конце вывести все стадии, разделенные знаком =>, 
# что будет означать постепенный переход от одного к другому.

# Australopithecus
# Homo habilis 
# Homo erectus 
# Homo neanderthalensis 
# Homo sapiens sapiens


print("Укажите по порядку этапы развития человека")

print("1 этап:")
stage1 = input()

print("2 этап:")
stage2 = input()

print("3 этап:")
stage3 = input()

print("4 этап:")
stage4 = input()

print("5 этап:")
stage5 = input()

print(stage1,stage2,stage3,stage4,stage5,sep='=>')
