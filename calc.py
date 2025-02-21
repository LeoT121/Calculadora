def sumar():
    x, y
    
def restar():
    x, y

def multiplicar():
    x, y

def dividir():
    x = float(input("Ingresa el primer numero: "))
    y = float(input("Ingresa el segundo numero: "))
    
    res = x/y;
    
    print("Resultado de la division: ", res)

def potencia():
    x, y

def raiz():
    x, y

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
    
