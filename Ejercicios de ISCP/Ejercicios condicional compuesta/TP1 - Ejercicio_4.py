# Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.

numero= int(input("elija un numero del 1 al 7 : "))

if(numero>=1):
    if(numero<=7):
        if(numero==1):
            print("El numero elegido corresponde al dia lunes")
        elif(numero==2):
            print("El numero elegido corresponde al dia martes")
        elif(numero==3):
            print("El numero elegido corresponde al dia miercoles")
        elif(numero==4):
            print("El numero elegido corresponde al dia jueves")
        elif(numero==5):
            print("El numero elegido corresponde al dia viernes")
        elif(numero==6):
            print("El numero elegido corresponde al dia sabado")
        elif(numero==7):
            print("El numero elegido corresponde al dia domingo")
    else:
        print("Numero INCORRECTO")
else:
    print("Numero INCORRECTO")