def sumar():
    x = float(input("Ingresa el primer numero\n"))
    y = float(input("Ingresa el segundo numero\n"))
    res = x + y
    print("El resultado de la suma es: ")
    print(res)

    
def restar():
    x, y

def multiplicar():
    x, y

def dividir():
    x, y

def potencia():
    x, y

def raiz():
    x, y

f = 1
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
    