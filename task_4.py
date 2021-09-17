# -*- coding: utf-8 -*-
def calculate_angle(hours, minutes):
    angle = abs((hours+(minutes/60))*30 - minutes*6)
    return min(360-angle,angle)

def get_parametr():
    hours = int(input("Введите часы от [1, 12]: "))
    minutes = int(input("Введите минуты от [0, 59]: "))
    if hours in range(1,13) and minutes in range(0,60):
        print(calculate_angle(hours, minutes))
    else:
        print('Повторите попытку')
        get_parametr()

get_parametr()


