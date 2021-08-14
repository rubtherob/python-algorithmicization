#4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

n = int (input ('Введите кол-во элементов ряда'))
first = 1
summ = 0
for i in range (n):
    if i % 2 == 0:
        summ += first
        first=first/2
    if i % 2 != 0:
        summ -= first
        first = first / 2
print(summ)