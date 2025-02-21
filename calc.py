def sumar():
    x, y

    
def restar():
    x, y = 0

def multiplicar():
    x, y = 0

def dividir():
    x, y = 0

def potencia():
    x, y = 0

def raiz():
    print("Ingrese el número a sacar raíz cuadrada:")
    x = float(input())
    raiz = pow(x, 0.5)
    print(f"La raíz cuadrada de {x} es:{raiz}")


f = 1
while f == 1:
    opcion = 1
    print("Menu de calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz")
    print("7. Salir")
    input(opcion)
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
    elif(opcion == 6):
        f = 0
    else:
        print("Opcion invalida")
    