n1 = -1
while int(n1) < 0  or int(n1) >100 :
     try:     
         n1 = int(input ("Введите первое число от 1 до 100: "))
     except ValueError:
         print ( "Ошибка ")
         
n2 = -1           
while int(n2) < 0  or int(n2) >100 :
     try:  
         n2 = int(input ("Введите второе число от 1 до 100: "))
     except ValueError:
         print ( "Ошибка ")
         
try:
    rez = round( n1 / n2,3)
    print ( "Результат: " ,rez)
except ZeroDivisionError:
    print ( "Ошибка ")
 


   
   
     





 
