def run():
    sumar = lambda x,y: x + y
    resta = lambda x,y: x - y
    division = lambda x,y: x / y
    multiplicacion = lambda x,y: x * y

    print(""" ELIGE QUE QUIERES HACER CON TUS DOS VALORES
                1-SUMA
                2-RESTA
                3-MULTIPLICACION
                4-DIVISION """)

    valor =int(input("Escoge: "))
    if valor > 0 and valor < 5:
        x = int(input("Escribe el primer valor: "))
        y = int(input("Escribe el segundo valor: "))
    else:
        print("CHUPALO!!!")
    print(""" EL RESULTADO DE LA OPERACION ES: """)

    if valor == 1:
        print(sumar(x, y))
    elif valor == 2:
        print(resta(x, y))
    elif valor == 3:
        print(multiplicacion(x, y))
    elif valor == 4:
        print(division(x, y))

if __name__ == '__main__':
    run()
