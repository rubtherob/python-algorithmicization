#4. Написать программу, которая генерирует в указанных пользователем границах: случайное целое число;
# случайное вещественное число; случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
#  Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
from random import random

m1 = int(input('Введите целое число'))
m2 = int(input('Введите целое число'))
n = int(random() * (m2 - m1 + 1)) + m1
print(n)

m1 = float(input('Введите не целое число'))
m2 = float(input('Введите не целое число'))
n = random() * (m2 - m1) + m1
print(round(n, 3))

m1 = ord(input('Введите символ'))
m2 = ord(input('Введите символ'))
n = int(random() * (m2 - m1 + 1)) + m1
print(chr(n))
