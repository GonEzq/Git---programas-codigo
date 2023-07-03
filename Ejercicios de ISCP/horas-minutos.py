def conversion(horas,minutos,segundos):
    totalSegundos = horas * 3600 + minutos * 60 + segundos
    print ( "Total de segundos: " ,totalSegundos)
conversion(30,16,12)


#Realice un programa que contenga una función que se llame “conversion”, 
#que la misma contenga tres parámetros. Se pide convertir los segundos ingresados en horas, minutos y segundos

def conversion(segundos):
    horas = segundos // 3600
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60
    segundos_finales = segundos_restantes % 60
    return horas, minutos, segundos_finales

# Uso
print("----------------------------")
segundos_t = int(input("Ingresa la cantidad de segundos: "))

horas, minutos, segundos = conversion(segundos_t)
print("----------------------------")
print(f"{segundos_t} segundos equivale a: {horas} horas, {minutos} minutos, {segundos} segundos.")
print("----------------------------")

