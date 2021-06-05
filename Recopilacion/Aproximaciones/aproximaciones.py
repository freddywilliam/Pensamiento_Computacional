objetivo = int(input("Ingresa numero: "))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo) + respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print("No se encontro la raiz cuadrada de " + str(objetivo))
else:
    print("La raiz cuadrada de " + str(objetivo) + " es " + str(respuesta))