import random


res1 = {(0): 'ноль быков',
       (1): 'один бык есть',
       (2): 'два быка',
       (3): 'уже три быка',
       (4): 'четыри быка. Молодцы!'}
res2 = {(0): 'и ноль коров. Пробуйте еще!',
       (1): 'и плюс одна корова)))',
       (2): 'и две коровы, уже где то близко отгадка!',
       (3): 'и коров уже три!!!',
       (4): 'и вы собрали четыри коровы!'}
       
r = '0123456789'
print('Добро пожаловать в игру "Были и Коровы!"\nЕсли устанете во время игры просто напишите "Я сдаюсь!"\nНачнем Игру!!! ') 
num = (random.choice(r)) + (random.choice(r))+ (random.choice(r))+(random.choice(r))

print(num)

while True:
    byk = 0
    cor = 0 
    igr1 = str(input('Введите комбинацию 4-х цифр: '))
    if igr1.lower() == 'Я сдаюсь!':
       print('До свидание! Приходите еще поиграть!') 
       break
    elif num == (igr1):
         print ('Ура! Поздравляю!!! Вы угодали!!!')
         break  
    else:       
       if len(igr1) != 4 :
          print('Нужно вести четыри цифры!')      
       else:
          for i in range(4):            
             if num[i] == igr1[i]:
                byk += 1
             elif igr1[i] in num: 
                cor += 1
              
          print ('В вашей догатке ',res1[(byk)],res2[(cor)] )
                     
               
        

   

 





    

   
    

