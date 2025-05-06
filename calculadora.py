from operaciones import suma
from operaciones import resta
from operaciones import division
from operaciones import multiplicacion

operacion = input ("ingrese la operacion a realizar: suma, resta, multiplicacion, division:")
operacion = operacion.lower()

try:
    if operacion =="suma":
        a = int(input("ingrese el primer numero:"))
        b = int(input("ingrese el segundo numero:"))
        print(suma(a,b))        
    elif operacion == "resta":
        a = int(input("ingrese el primer numero:"))
        b = int(input("ingrese el segundo numero:"))
        print(resta(a,b))
    elif operacion == "multiplicacion":
        a = int(input("ingrese el primer numero:"))
        b = int(input("ingrese el segundo numero:"))
        print(multiplicacion(a,b))
    elif operacion == "division":
        a = int(input("ingrese el primer numero:"))
        b = int(input("ingrese el segundo numero:"))
        print(division(a,b))    
except ValueError:
    print("Debe ingresar un numero entero")
        
except ZeroDivisionError:
    print("No se puede dividir entre cero")        

