import random
n1 = -1
print ( "Игра угадай число.")
def fun():
    while int(n1) < 0  or int(n1) >10:
         try:  
             return  int(input ("Введите число  от 0 до 10 = "))
         except ValueError:
              print ( "Ошибка ")

r = random.randint(1,10)

while r != n1:
      n1 = -1
      n1 = fun()
      if n1 > r:
         print ( "Ваше число больше")          
      elif n1 < r:
        print ( "Ваше число меньше")    
      else:
          print ( "Ура!!!")
          continue

