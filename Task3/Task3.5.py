#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
a=[]

list_index=[]
for i in range (6):
   a.append(int(input()))


for i in range (len(a)):
    if a[i] < 0:
        list_index.append(i)
maxx = a[list_index[0]]
for i in range (len(list_index)):
    if maxx < a[list_index[i]]:
        maxx = a[list_index[i]]

print(maxx)

