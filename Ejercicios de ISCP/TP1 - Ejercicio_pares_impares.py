# realize un programa que lea 4 numeros y diga cuantos pares son y cuantos impares y devuelva la sumatoria de los pares

contador = 0
pares = 0
suma_pares = 0

while contador < 4:
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        pares += 1
        suma_pares += numero
    contador += 1

impares = 4 - pares

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Suma de los números pares:", suma_pares)