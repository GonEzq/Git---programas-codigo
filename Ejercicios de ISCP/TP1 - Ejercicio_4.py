#4.Leer 10 números y mostrar solamente los números positivos, y su sumatoria.

numeros = []
for i in range(10):
    numeros.append(int(input("Ingrese un número: ")))

numeros_positivos = [numero for numero in numeros if numero > 0]
sumatoria_positivos = sum(numeros_positivos)

print("Números positivos:", numeros_positivos)
print("Sumatoria de los números positivos:", sumatoria_positivos)

#5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos
#números.

numeros_negativos = []
for i in range(15):
    numero = int(input("Ingrese un número negativo: "))
    if numero < 0:
        numeros_negativos.append(numero)
    else:
        print("Este número no es negativo. Ingrese uno negativo.")
        i -= 1

numeros_positivos = [-numero for numero in numeros_negativos]
print("Números positivos correspondientes:")
print(numeros_positivos)