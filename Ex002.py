# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

number = int(input('Введите натуральное число: '))

def simple_numbers(n):
    lis = []
    d = 2
    while n != 1:
        if n % d == 0:
            lis.append(d)
            n //= d
            d = 2
        else:
            d += 1
    return lis

print(simple_numbers(number))
