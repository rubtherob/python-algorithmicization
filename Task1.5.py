#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
a=ord(input('Введите букву').lower())
b=ord(input('Введите вторую букву букву').lower())
print('Место первой буквы ',int(a)-ord('a')+1)
print('Место второй буквы ',int(b)-ord('a')+1)
print(f"Между первой и второй буквой {(int(b)-ord('a')+1)-((int(a)-ord('a')+1))-1} букв")