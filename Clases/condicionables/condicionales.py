x = 1
#comparar si un valor es igual (==)
if(x == 2):
    print("Correcto")
else:
    print("incorrecto")    
#comparar si un valor es mayor o igual (>=)
if(x >= 2):
    print("Correcto")
else:
    print("incorrecto")

#comparar si un valor es menor o igual (<=)
if(1 <= 2):
    print("Correcto")
else:
    print("incorrecto")

#comparar si un valor es mayor (>)
if(x > 2):
    print("Correcto")
else:
    print("incorrecto")

#comparar si un valor es menor (<)
if(x < 2):
    print("Correcto")
else:
    print("incorrecto")

#comparar si un valor es diferente (!=)
if(x != 2):
    print("Correcto")
else:
    print("incorrecto")  

###########################//Ejercicio condicionales//################################
#if anidado
numero1 = int(input("Ingresa: "))

if(numero1 >0):
    print("Es positivo")

elif(numero1 <0):
    print("Es negativo")

else:
    print("Es cero")

#######identifica si es par o impar

numero = int(input("Igresa un numero:  "))

if (numero%2 == 0):
    print("El numero {0} par, {1}".format(numero,"gracias"))
else:
    print("El numero {0} es impar".format(numero))    