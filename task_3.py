# -*- coding: utf-8 -*-
class BaseConverter():
    def convert(self, num, unit_of_measure):
        unit_of_measure = unit_of_measure.lower()
        if unit_of_measure == 'k':
            k = 273.15
            return num + k
        if unit_of_measure == 'f':
            return ((9 * num) / 5 ) + 32
        if unit_of_measure == 'r':
            return (num * 4) / 5
        else:
            return 'Повторите попытку'

# считываем данные
num = float(input("Введите значение температуры в градусах по Цельсию: "))
unit_of_measure = input("Введите шкалу для конвертации(Кельвины - К, Фаренгейты - F, Реомюра - R): ")

# вызыввем функцию и печатаем результат
class_obj = BaseConverter()
print(class_obj.convert(num, unit_of_measure))

