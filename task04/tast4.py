import re
parol = input("Введите пароль: ")

import random

def f():
    st2 = ''
    i = 0
    r = '123456789'
    list1 ='qwertyuiopasdfghjklzxcvbnm'
    list3 = list1.upper()
    list2 = '+-/*!&$#?=@<>_'
    st = list1 + list2 + list3 + str(r)    
    for i in range(10):   
       st2 = st2 + (random.choice(st))    
 
    st3 = list(st2 + random.choice(r) + random.choice(list1) + random.choice(list2) + random.choice(list3))
    random.shuffle( st3)
    s = ''.join(st3)
    return s  

if len(parol) >= 8:
    if re.search(r'[A-Z]',parol):               
       if re.search('\d+', parol) is not None:
           if not set(parol).isdisjoint(set('+-/*!&$#?=@<>_')):
               print ("Пароль правильный)")               
           else:
            print ("Пароль не содержит спец.знак")
            print ("Предлагаю вам новый пароль: ", f() )                        
       else:
            print ("Пароль не содержит цифр")
            print ("Предлагаю вам новый пароль: ", f() )       
       
    else:
         print ("Пароль не содержит заглавную букву")     
         print ("Предлагаю вам новый пароль: ", f() )
else:
    print ("Пароль должен содержать  8-м и  более символов")

   
    

