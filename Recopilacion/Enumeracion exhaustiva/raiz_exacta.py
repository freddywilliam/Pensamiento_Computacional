
objetivo = int(input("Ingresa tu numero: "))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1

if respuesta**2 == objetivo:
    print("La raiz cuadrada de " + str(objetivo) + " es " + str(respuesta))
else:
    print("La raiz cuadrada de " + str(objetivo) + " no es exacta. ")