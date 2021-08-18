#4. Определить, какое число в массиве встречается чаще всего
a=[]
for i in range (6):
   a.append(int(input()))
max_numb = a[0]
max_copy = 0
count = 0
for i in a:
    for j in a:
        if i == j:
            count += 1
    if count > max_copy:
        max_copy=count
        max_numb = i
    count = 0

print ('Число которое встречается больше всего=',max_numb,'   ','Встречется раз',max_copy)
