#5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa

precio_del_dolar= 460
print ("Que tipo de convesion quiere hacer?")
print ("1- Pesos ARG a USD")
print ("2- USD a pesos ARS")
opcion=int(input("Opcion: "))

if(opcion== 2):
    valor_dolar= float(input("Ingrese su valor en dolares: "))
    conversion= valor_dolar * precio_del_dolar
    print("Los {:.2f} USD equivalen a {:.2f} ARS".format(valor_dolar,conversion))
elif(opcion ==1):
    valor_pesos= float(input("ingrese su valor en pesos: "))
    conversion= valor_pesos / precio_del_dolar
    print("Los {:.2f} ARS equivalen a {:.2f} USD".format(valor_pesos,conversion))
else:
    print ("Ingrese una opcion correcta")

