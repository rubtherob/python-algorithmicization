#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
#  Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
def sort_bubble(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1 - i):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)



import random

a = [0] * 10
for i in range(10):
    a[i]+=random.randrange(-100, 100)
print(a)

sort_bubble(a)