# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('Homework4\poly_1.txt', 'r', encoding='utf-8') as input_1, \
    open('Homework4\poly_2.txt', 'r', encoding='utf-8') as input_2:
    file_1=input_1.readlines()
    file_2=input_2.readlines()
    result = ''
    if len(file_1)==len(file_2):
        for i, k in enumerate(file_1):
            with open('Homework4\poly_3.txt', 'a', encoding='utf-8') as output:
                output.write(f'{k[0:-5]} + {file_2[i]}')
    else:
        print('Ошибка! Файлы содержат разное количество строк.')