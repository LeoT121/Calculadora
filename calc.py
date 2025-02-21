def sumar():
    x, y

    
def restar():
    x, y

def multiplicar():
    x, y

def dividir():
    x, y

def potencia():
    x = float(input("Ingresa el número base: "))
    y = float(input("Ingresa el exponente: "))
    resultado = pow(x, y)
    print(f"El resultado de {x} elevado a la potencia de {y} es: {resultado}")


def raiz():
    x, y

while f == 1:
    print("Menu de calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz")
    print("7. Salir")
    opcion = int(input("ingresa la opcion\n"))
    if(opcion == 1):
        sumar()
    elif(opcion == 2):
        restar()
    elif(opcion == 3):
        multiplicar()
    elif(opcion == 4):
        dividir()
    elif(opcion == 5):
        potencia()
    elif(opcion == 6):
        raiz()
    elif(opcion == 7):
        f = 0
    else:
        print("Opcion invalida")
