import random
byk = 0
cor = 0
r = '0123456789'
print('  Добро пожаловать в игру "Были и Коровы"! ') 
num = (random.choice(r)) + (random.choice(r))+ (random.choice(r))+(random.choice(r))

print(num)

igr1 = str(input('Введите комбинацию 4-х цифр: '))
if not 999 < int(igr1) < 10000 :
   print('Нужны цифры от 1000 to 9999')
else:
   for i in range(4):            
       if num[i] == igr1[i]:
          byk += 1
       elif igr1[i] in num: 
          cor += 1
print ('byk', byk, 'cor', cor)                      
                     
               
        

   

 





    

   
    

