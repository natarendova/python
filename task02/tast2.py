import random
n1 = -1
print ( "Игра угадай число.")
mx = int(input('Максимальное: '))
r = random.randint(1,mx)
i = 1

def fun():
    while int(n1) < 0  or int(n1) > mx:
         try:  
             return  int(input ("Введите число  от 0 до {}  " .format(mx)))
         except ValueError:
              print ( "Ошибка ")
while i < 6: 
      while r != n1:
            n1 = -1      
            n1 = fun()         
      
            if n1 > r:
               print ( "Ваше число больше")
               i += 1
            elif n1 < r:
                 print ( "Ваше число меньше")
                 i += 1
            else:
                 print ( "Ура!!!Вы угодали c {}-й попытки".format(i))
            break
if i == 6:
   print ( "Попытки закончились!!!")
