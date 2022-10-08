# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

import random

def creat_rand_list():
    n = int(input('Введите размер списка: '))
    while n <= 0:
        print('Введён неверный размер списка')
        n = int(input('Введите размер списка: '))
    lis = []
    for i in range(n):
        lis.append(random.randint(1, 10))
    return lis

def non_repeating_elements(lis):
    result = []
    for i in range(len(lis)):
        count =0
        for k in range(len(lis)):
            if lis[i] == lis[k]:
                count+=1
        if count ==1:
            result.append(lis[i])
    return result

create = creat_rand_list()
print(create)
print(non_repeating_elements(create))
