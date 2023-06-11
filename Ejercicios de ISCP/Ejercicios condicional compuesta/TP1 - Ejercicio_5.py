# Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.

numero= int(input("elija un numero del 1 al 12 : "))

if(numero>=1):
    if(numero<=12):
        if(numero==1):
            print("El numero elegido corresponde al dia enero")
        elif(numero==2):
            print("El numero elegido corresponde al dia febrero")
        elif(numero==3):
            print("El numero elegido corresponde al dia marzo")
        elif(numero==4):
            print("El numero elegido corresponde al dia abril")
        elif(numero==5):
            print("El numero elegido corresponde al dia mayo")
        elif(numero==6):
            print("El numero elegido corresponde al dia junio")
        elif(numero==7):
            print("El numero elegido corresponde al dia julio")
        elif(numero==8):
            print("El numero elegido corresponde al dia agosto")
        elif(numero==9):
            print("El numero elegido corresponde al dia septiembre")
        elif(numero==10):
            print("El numero elegido corresponde al dia octubre")
        elif(numero==11):
            print("El numero elegido corresponde al dia noviembre")
        elif(numero==12):
            print("El numero elegido corresponde al dia diciembre")
    else:
        print("Numero INCORRECTO")
else:
    print("Numero INCORRECTO")