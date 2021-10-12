n1 = input("Введите первое число от 1 до 100: ")
try:
     n1 = int(n1)
except ValueError:
     n1 = input ("Введите первое число от 1 до 100: ")
     

if  int(n1) < 0  or int(n1) >100:
     n1 = input ("Введите первое число от 1 до 100: ")
else:    
     n1 = n1
          
     
n2 = input("Введите второе число от 1 до 100: ")
try:
     n2 = int(n2)
except ValueError:
     n2 = input ("Введите второе число от 1 до 100: ")
     

if  int(n2) < 0  or int(n2) >100:
     n2 = input ("Введите первое число от 1 до 100: ")
else:    
     n2 = n2
     

if n1 > n2:
     # rez = (n1 / n2)
      print ( "Результат: " ,round( n1 / n2,3))
elif n1 == n2:
      print ( "Результат: " ,round( n1 / n2,3))
else:
      #rez = (n2 / n1) 
      print ( "Результат: ",round( n2 / n1,3))  



 
