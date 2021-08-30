#1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
import sys
import random

a=[]

list_index=[]
for i in range (6):
   a.append(random.randrange(-100,100))


for i in range (len(a)):
    if a[i] < 0:
        list_index.append(i)
maxx = a[list_index[0]]
for i in range (len(list_index)):
    if maxx < a[list_index[i]]:
        maxx = a[list_index[i]]


sum_byte=(sys.getsizeof(maxx) + sys.getsizeof(list_index) + sys.getsizeof(a))

print('Кол-во байт выделеных на все переменные в первом алгоритме:',sum_byte)


a=[]
b=[]
for i in range (6):
   a.append(random.randrange(0,100))

for j in range (len(a)):
    if a[j] % 2 == 0:
        b.append(j)



sum_byte=(sys.getsizeof(b) + sys.getsizeof(a))
print('Кол-во байт выделеных на все переменные во втором алгоритме:',sum_byte)