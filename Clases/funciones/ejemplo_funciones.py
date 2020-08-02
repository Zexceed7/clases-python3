def ejemplo():
    lista=[1,2,3,4,5,6,7]
    for numero in lista:
        print("tu numero es: ", numero)

def ejemplo2 (numero1, numero2):
    print("tu suma es: ", numero1+numero2)



def menu():
    print("BIenvenido al menu!!!")
    opcion = int(input("Ingresa una opcion: "))

    if opcion==1:
        ejemplo()
    else:
        ejemplo2(5,4)

menu()        









