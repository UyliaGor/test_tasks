# -*- coding: utf-8 -*-
import random

numbers = []
for _ in range(10):
    num = random.random()
    numbers.append(num)

print('Максимальное значение =', max(numbers))
print('Минимальное значение =', min(numbers))
print('Среднее значение', sum(numbers)/len(numbers))
