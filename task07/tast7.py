import random
byk = 0
cor = 0


print('  Добро пожаловать в игру "Были и Коровы"! ')
num = random.randint(1000,9999)
num = str(num)
print(num)
while True:
     igr1 = (input('Введите комбинацию 4-х цифр: '))
     if not 999 < int(igr1) < 10000 :
           print('Нужны цифры от 1000 to 9999')
     else:
         print("Нhhhh")
         for i in set(num) and set(igr1):
            
            if num.find(i) == igr1.find(i):
               byk += 1
            else:
                cor += 1
print ('byk', byk, 'cor', cor)                      
                     
               
        

   

 





    

   
    

