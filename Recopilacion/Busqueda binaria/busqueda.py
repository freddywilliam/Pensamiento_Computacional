 
objetivo = int(input("Escoge un numero: "))
epsilon = 0.01
bajo = 0.0
alto = max(1.0 , objetivo)
respuesta = (alto + bajo / 2)
while abs(respuesta**2 - objetivo) >= epsilon:
    print("Bajo " + str(bajo) + " Alto " + str(alto) + " Respuesta "+ str(respuesta) )
    if respuesta**2 < objetivo:
       bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo) / 2
print("La raiz cuadrada de " + str(objetivo) + " es " + str(respuesta))

