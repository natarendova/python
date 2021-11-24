import re
import random

parol = input("Введите пароль: ")

def fun(h=len(parol)-4):
    st2 = ''
    i = 0
    r = '123456789'
    list1 ='qwertyuiopasdfghjklzxcvbnm'
    list3 = list1.upper()
    list2 = '+-/*!&$#?=@<>_'
    st = list1 + list2 + list3 + str(r)    
    for i in range(h):   
       st2 = st2 + (random.choice(st))    
 
    st3 = list(st2 + random.choice(r) + random.choice(list1) + random.choice(list2) + random.choice(list3))
    random.shuffle( st3)
    s = ''.join(st3)
    return s  

if len(parol) >= 8:
    if not re.search(r'[A-Z]',parol):
       print ("Пароль не содержит заглавную букву")  
    elif not re.search('\d+', parol):
       print ("Пароль не содержит цифр")
    elif set(parol).isdisjoint(set('+-/*!&$#?=@<>_')):
        print ("Пароль не содержит спец.знак")   
    else:
        print ("Пароль правильный)")             
else:
    print ("Пароль должен содержать  8-м и  более символов")

if re.search(r'[A-Z]',parol) or re.search('\d+', parol) or not set(parol).isdisjoint(set('+-/*!&$#?=@<>_')):
        print ("Предлагаю вам новый пароль: ", fun() )    

    

   
    

