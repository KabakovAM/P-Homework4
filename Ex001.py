# 1. Вычислить число c заданной точностью d

from decimal import Decimal

n = float(input('Введите число: '))
d = str(input('Введите необходимую точность (например 0.0001): '))
number = Decimal(n)
print(number.quantize(Decimal(d)))
