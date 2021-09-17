# -*- coding: utf-8 -*-
import math

def f(x):
    return math.cos(x**5) + x**4 - 345.3 * x - 23

def half_interval(a, b, e):
    if abs(f(a)) < e:
        return a
    elif abs(f(b)) < e:
        return b
    c = (a + b) / 2.0
    if abs(f(c)) < e:
        return c
    if f(a)*f(c) <= 0.0:
        return half_interval(a, c, e)
    else:
        return half_interval(c, b, e)

print("Корень равен:", half_interval(0, 10, 0.001))



