#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a=int(input())
b=int(input())
c=int(input())


if (b < a < c) or (c < a < b):
    print('Среднее:', a)
elif (a < c < b) or (b < c < a):
    print('Среднее:', c)
else:
    print('Среднее:', b)