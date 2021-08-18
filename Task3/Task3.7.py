#7. В одномерном массиве целых чисел определить два наименьших элемента.
#  Они могут быть как равны между собой (оба являться минимальными), так и различаться.

a=[]



for i in range (6):
   a.append(int(input()))

min1=a[0]
index_min=0
for i in range(len(a)):
    if a[i]<min1:
        min1=a[i]
        index_min=i


min2=a[1]
for i in range(len(a)):
    if a[i]<min2 and i!=index_min:
        min2=a[i]


print(min1,min2)