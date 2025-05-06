from operaciones import suma
from operaciones import resta
from operaciones import division
from operaciones import multiplicacion
from operaciones import potencia
from operaciones import divisionEntera

operacion = input ("ingrese la operacion a realizar: \n suma: +\n resta: -\n multiplicacion: *\n division: /\n potencia:**\n divEntera: // \n")
operacion = operacion.lower()

try:
    if operacion =="+":
        a = int(input("ingrese el primer numero:"))
        b = int(input("ingrese el segundo numero:"))
        print(suma(a,b))  
    elif operacion == "-":
        a = int(input("ingrese el primer numero:"))
        b = int(input("ingrese el segundo numero:"))
        print(resta(a,b))
    elif operacion == "*":
        a = int(input("ingrese el primer numero:"))
        b = int(input("ingrese el segundo numero:"))
        print(multiplicacion(a,b))
    elif operacion == "/":
        a = float(input("ingrese el primer numero:"))
        b = float(input("ingrese el segundo numero:"))
        print(division(a,b))  
    elif operacion == "**":
        a = int(input("ingrese el primer numero:"))
        b = int(input("ingrese el segundo numero:"))
        print(potencia(a,b))
    elif operacion == "//":
        a = int(input("ingrese el primer numero:"))
        b = int(input("ingrese el segundo numero:"))
        print(divisionEntera(a,b))
except ValueError:
    print("Debe ingresar un numero")
       
except ZeroDivisionError:
    print("No se puede dividir entre cero")        
