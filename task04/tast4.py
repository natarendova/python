import re

parol = input("Введите пароль: ")  


if len(parol) >= 8:
    if re.search(r'[A-Z]',parol) and re.search('\d+', parol) is not None and not set(parol).isdisjoint(set('+-/*!&$#?=@<>_')):        
       print ("Пароль хороший)")
    else:
       print ("Пароль не содержит заглавную букву, или цифр, или спец.знаков")
       
else:
    print ("Пароль должен содержать  8-м и  более символов")
    
print (parol)
