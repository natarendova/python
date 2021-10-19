n1 = -1
n2 = -1
def fun():
    while int(n1) < 0  or int(n1) >100  or int(n2) < 0  or int(n2) >100:
         try:  
             return  int(input ("Введите  число от 1 до 100: "))
         except ValueError:
              print ( "Ошибка ") 
    
n1 = fun()  
n2 = fun()     
         
try:
    rez = round( n1 / n2,3)
    print ( "Результат: " ,rez)
except ZeroDivisionError:
    print ( "Ошибка ")
 


   
   
     





 
