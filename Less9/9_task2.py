# Вводятся два списка чисел, которые могут содержать до 100000 чисел каждый. 
# Все числа каждого списка находятся на отдельной строке. 
# Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором.

# заполнить 1 список

N = int(input())
n_list = [] 
for i in range(N):
    n_list.append( int(input()) )

# заполнить 2 список
M = int(input())
m_list = [] 
for i in range(M):
    m_list.append( int(input()) )  
  
#преобразуем списки к множеству
n_set = set(n_list) 
m_set = set(m_list) 

#через пересечение найдем результат
print(len(n_set.intersection(m_set)))



