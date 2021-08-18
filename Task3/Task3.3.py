#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
a=[]
max_list=[]
min_list=[]
#Заполняем массив
for i in range (6):
   a.append(int(input()))
# Поиск макс и мин
minn=a[0]
maxx=a[0]
for i in range (len(a)):
    if maxx<a[i]:
        maxx=a[i]
    elif minn>a[i]:
        minn=a[i]
#Поиск копий макс и мин
for i in range (len(a)):
    if maxx == a[i]:
        max_list.append(i)
    elif minn == a[i]:
        min_list.append(i)


#Замена всех мин на макс и наоборот
for i in max_list:
    a[i]=minn
for i in min_list:
    a[i]=maxx

print (a)
