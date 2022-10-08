# 4.* Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.

import random

def polynomial_in_file():
    k = int(input('Введите натуральную степень k: '))
    while k <= 0:
        print('Введёно неправильное число.')
        k = int(input('Введите натуральную степень k: '))
    result = ''
    for i in range(k, -1, -1):
        a = random.randint(0, 10)
        if a != 0:
            if i == 0:
                result += (f'{a} ')
            else:
                result += (f'{a}*x^{i} {random.choice("-+")} ')
    if result[-2] == '-' or result[-2] == '+':
        result = result[0:-2]
    if len(result) <= 2:
        result = (f'{result}= {result}')
    else:
        result += '= 0'
    with open('Homework4\poly_0.txt', 'a', encoding='utf-8') as output:
        output.write(f'{result}\n')

for i in range(3):
    polynomial_in_file()