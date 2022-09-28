# -*- coding: utf-8 -*-
import random
from bs4 import BeautifulSoup
# Аби не ускладнювати собі задачу, треба уважно читати умову, аби не придумовувати лишній функціонал
# \(backslash) символ продовження строки
# /a -звук системного динаміка
# print("I'am the best \
# coder")
# output run after tuch enter
# input("Чтобы узнать, нажмите Enter")
# print("19 / 4 =", 19 / 4)
# вивод 19 / 4 = 4,75

# 9//4 >>2
# 9/4 >> 2,25
# 9%4 >>1
# Поддержку точной десятичной арифметики для дробных
# чисел осуществляет модуль decimal. Подробнее о нем можно прочесть в документации Python.

# def positive():
#     print("Положительное")
#
# def negative():
#     print("Отрицательное")
#
# def test():
#     integer = int(input("Введите целое число: "))
#     if integer > 0:
#         positive()
#     else:
#         negative()
#
# test()

# глава 3, задача 1
# surprise = random.randint(1, 5)
# choice = ''
# while surprise != choice:
#     surprise = random.randint(1, 5)
#     choice = input('Введите выбрать: ')
#     if surprise == 1:
#         print("Banana")
#     elif surprise == 2:
#         print("Apple")
#     elif surprise == 3:
#         print("Pineapple")
#     elif surprise == 4:
#         print("Cherry")
#     else:
#         print("Orange")


# counter_1 = 0
# counter_2 = 0
# coin = 0
# while coin != 100:
#     coin += 1
#     result = random.randint(0, 1)
#     if result == 0:
#         counter_1 += 1
#     else:
#         counter_2 += 1
# print("Орел выпал " + str(counter_1) + " раз, а решка " + str(counter_2) + "раз")


# print('Я загадал целое число от 0 до 100. Угадай с 5 попыток!')
# digit = random.randrange(101)
# popitka_count = 0
# while popitka_count <= 4:
#     popitka_count += 1
#     popitka = int(input('Это число: '))
#     if popitka < digit:
#         print('Больше!')
#     elif popitka > digit:
#         print('Меньше!')
#     else:
#         print('Ничего себе! Ты отгадал! Это правда', digit)
#         print('Количество попыток:', popitka_count)
#         break
# if popitka_count == 5 and popitka != digit:
#     print('О, ужас! Ты совершенно не умеешь читать мои мысли!\n\
#     Так и не смог угадать число за 5 попыток :(')

# low_num = 0
# high_num = 100
# result = 50
# count = 1
# while digit != result:
#     count += 1
#     digit = random.randrange(0, 100)
#     if result > digit:
#         low_num = digit + 1
#     else:
#         high_num = digit - 1
# print("Для отгадывания вам понадобилось " + str(count) + " попыток")

# print('Загадай любое целое число от 1 до 100. \
# А я его отгадаю. Говори мне </>. \
# Когда я угадаю, напиши "yes"\n')
# input('Нажми Enter, когда загадал')
# low_num = 0
# high_num = 100
# gues = random.randint(low_num, high_num)
# print('Это число', gues, '?')
# otvet = input('Угадал?\n')
# while otvet != 'y':
#     if otvet == '<':
#         high_num = gues-1
#         gues = random.randint(low_num, high_num)
#         print(gues)
#         otvet = input('Угадал?\n')
#     elif otvet == '>':
#         low_num = gues+1
#         gues = random.randint(low_num, high_num)
#         print(gues)
#         otvet = input('Угадал?\n')
# input('Ура! Я отгадал! Нажми Enter, чтобы выйти.')

# OR

# Bisection method

# begin = 0
# end = 100
# guess = ""
#
# print("I'll guess a number 1-100.. answer 'yes' if I correct \
# and 'less' or 'more' if number is bigger or smaller\n")
#
# while True:
#     guess = (begin + end) // 2
#     print("Is it", int(guess), "?")
#     answer = input()
#     if answer == "yes" or (end - begin == 2):
#         break
#     if answer == "more":
#         begin = guess
#     elif answer == "less":
#         end = guess
#
# print("Number was ", guess, ". Good job!")
#
# input()

# Резчик пиццы
# Демонстрирует срезы строк
word = "пицца"
рrint("Введите начальный и конечный индексы для того среза 'пиццы'. который хотите
получить.")
print("Для выхода нажмите Enter. не вводя начальную позицию ")
start = None
while start != "":
    start = (input("\nНачальная позиция: "))
    if start:
        start = int(start)
        finish = int(input("Конечная позиция: "))
        print("Срез word[". start. ":". finish. "]")







