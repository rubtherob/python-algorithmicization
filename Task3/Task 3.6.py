#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#  Сами минимальный и максимальный элементы в сумму не включать.

a=[]
summ=0
list_index=[]
for i in range (6):
   a.append(int(input()))
index_min=0
index_max=0
minn=a[0]
maxx=a[0]
for i in range (len(a)):
    if maxx < a[i]:
        maxx = a[i]
        index_max = i
    elif minn > a[i]:
        minn = a[i]
        index_min = i


if index_max > index_min:
    for i in range (index_min+1,index_max):
        summ += a[i]
elif index_max < index_min:
    for i in range(index_max + 1, index_min):
        summ += a[i]

print(summ)