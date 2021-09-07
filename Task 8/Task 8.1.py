#1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
#  состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
import hashlib


s=str(input('Введите строку состоящюю из маленьких латинских букв: '))
number=1
count=1
array_hash=[]


while True:
    for i in range (len(s)):
        if hashlib.sha1(s[i : number].encode('utf-8')).hexdigest() not in array_hash:
            array_hash.append(hashlib.sha1(s[i : number].encode('utf-8')).hexdigest())
        if (number + 1) > len(s):
            break
        number += 1

    number = 1+ count
    count += 1
    if (number) > len(s):
        break
print(len (array_hash) )



