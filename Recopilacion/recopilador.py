def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:  
        respuesta += paso
    if abs(respuesta**2 - objetivo) >= epsilon:
        print("No se encontro la raiz cuadrada de " + str(objetivo))
    else:
        print("La raiz cuadrada de " + str(objetivo) + " es " + str(respuesta))

def raiz_exacta(objetivo):
    respuesta = 0
    while respuesta**2 < objetivo:
        respuesta += 1
    if respuesta**2 == objetivo:
        print("La raiz cuadrada de " + str(objetivo) + " es " + str(respuesta))
    else:
        print("La raiz cuadrada de " + str(objetivo) + " no es exacta. ")

def busqueda(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0 , objetivo)
    respuesta = (alto + bajo / 2)
    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
    print("La raiz cuadrada de " + str(objetivo) + " es " + str(respuesta))

def run():
    print(""" Elige la forma:

        1 - Busqueda
        2 - Raiz Exacta
        3 - Aproximacion
        
        """)

    valor = int(input("Ingresa el numero: "))
    if valor > 0 and valor < 4:
        objetivo = int(input("Escoge el numero para sacar su raiz cuadrada: "))
    else:
        print("Chupalo!!")

    if valor == 1:
        busqueda(objetivo)
    elif valor == 2:
        raiz_exacta(objetivo)
    elif valor == 3:
        aproximacion(objetivo)

if __name__ == '__main__':
    run()
