
#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random
M = 4
N = 4
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random()*200)
        b.append(n)
        print('%4d' % n,end='')
    a.append(b)
    print()

min_list=[]
for i in range(4):
    minn=a[0][i]
    for j in range(4):
        if a[j][i] < minn:
            minn=a[j][i]
    min_list.append(minn)

print(min(min_list))



