# leer 10 numeros y obtener la cantidad de mayores y la cantidad de menores a 100 , cual es el numero maximo y cual es el numero minimo

numeros = []
for i in range(10):
    numeros.append(int(input("Ingrese un número: ")))

cantidad_mayores = 0
cantidad_menores = 0
maximo = numeros[0]
minimo = numeros[0]
for numero in numeros:
    if numero > 100:
        cantidad_mayores += 1
    elif numero < 100:
        cantidad_menores += 1

    if numero > maximo:
        maximo = numero

    if numero < minimo:
        minimo = numero


print("Cantidad de números mayores a 100:", cantidad_mayores)
print("Cantidad de números menores a 100:", cantidad_menores)
print("Número máximo:", maximo)
print("Número mínimo:", minimo)