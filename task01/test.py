n1 = input("Введите первое число от 1 до 100: ")
try:
     n1 = int(n1)
except ValueError:
     n1 = input ("Введите первое число от 1 до 100: ")
     

if  int(n1) < 0  or int(n1) >100:
     n1 = input ("Введите первое число от 1 до 100: ")
else:    
     n1 = int(n1) 
           
n2 = input("Введите второе число от 1 до 100: ")
try:
     n2 = int(n2)
except ValueError:
     n2 = input ("Введите второе число от 1 до 100: ")
     

if  int(n2) < 0  or int(n2) >100:
     n2 = input ("Введите первое число от 1 до 100: ")
else:    
     n2 = int(n2)      

try:
    rez = round( n1 / n2,3)
    print ( "Результат: " ,rez)
except ZeroDivisionError:
    print ( "Ошибка ")



 
