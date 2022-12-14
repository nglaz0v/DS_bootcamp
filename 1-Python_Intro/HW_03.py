#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Реализуйте проверку ввода на число.
Программа должна выводить “Correct”, если введено целое или вещественное число
(в качестве разделителя должна использоваться одна точка).
Во всех остальных случаях должно выводиться “Wrong”.
Для выполнения задания необходимо изучить методы строк.
"""

x = input("Input a number: ")
if x.startswith('-'):  # если самый первый символ - знак 'минус'
    x = x[1:]  # то анализируем оставшуюся часть строки
x = x.replace('.', '', 1)  # заменим одну точку пустой строкой
if x.isdigit():
    print("Correct")
else:
    print("Wrong")
