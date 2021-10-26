import random
st2 = ''
i = 0
r = random.randint(1,10)
list1 ='qwertyuiopasdfghjklzxcvbnm'
list3 = list1.upper()
list2 = '+-/*!&$#?=@<>_'
st = list1 + list2 + list3 + str(r)

for i in range(10):
    #r1 = random.randint(1,50)
    st2 = st2 + (random.choice(st))
    #st2 = st2 + (st[r1])

print ("Пароль: ", st2 + str(r) + random.choice(list1) + random.choice(list2) + random.choice(list3) )
