#3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.

import random

# Inicializar contadores
mujeres = 0
varones = 0
mayores_de_edad = 0
menores_de_edad = 0

# Inicializar listas para almacenar las edades y el sexo de las personas
edades = []
sexo = []

# Ingresar de manera aleatoria las edades y el sexo de 15 personas
for _ in range(15):
    # Generar edad aleatoria entre 1 y 100
    edad = random.randint(1, 100)

    # Generar sexo aleatorio (0: mujer, 1: varón)
    sexo_persona = random.randint(0, 1)

    # Almacenar edad y sexo en las listas correspondientes
    edades.append(edad)
    sexo.append(sexo_persona)

    # Contar mujeres y varones
    if sexo_persona == 0:
        mujeres += 1
    else:
        varones += 1

    # Contar mayores y menores de edad
    if edad >= 18:
        mayores_de_edad += 1
    else:
        menores_de_edad += 1

# Imprimir los valores aleatorios generados
print("Valores aleatorios generados:")
for i in range(15):
    print("Persona", i+1, "- Edad:", edades[i], "Sexo:", "Mujer" if sexo[i] == 0 else "Varón")

# Imprimir los resultados
print("\nCantidad de mujeres:", mujeres)
print("Cantidad de varones:", varones)
print("Cantidad de personas mayores de edad:", mayores_de_edad)
print("Cantidad de personas menores de edad:", menores_de_edad)