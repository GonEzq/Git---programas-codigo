#4.Leer 10 números y mostrar solamente los números positivos, y su sumatoria.

numeros = []
for i in range(10):
    numeros.append(int(input("Ingrese un número: ")))

numeros_positivos = [numero for numero in numeros if numero > 0]
sumatoria_positivos = sum(numeros_positivos)

print("Números positivos:", numeros_positivos)
print("Sumatoria de los números positivos:", sumatoria_positivos)

