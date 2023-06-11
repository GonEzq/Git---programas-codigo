# Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.

print("Elija 3 numeros")
numero_1= int(input("Numero 1: "))
numero_2= int(input("Numero 2: "))
numero_3= int(input("Numero 3: "))

if(numero_1>numero_2):
    if(numero_1>numero_3):
        resto= numero_1 % 2
        if (resto==0):
            print ("El numero {} es el mayor y es par".format(numero_1))
        else:
            print ("El numero {} es el mayor y es impar".format(numero_1))    
    else:
        resto= numero_3 % 2
        if (resto==0):
            print ("El numero {} es el mayor y es par".format(numero_3))
        else:
            print ("El numero {} es el mayor y es impar".format(numero_3))  

elif(numero_2>numero_1):
    if(numero_2>numero_3):
        resto= numero_2 % 2
        if (resto==0):
            print ("El numero {} es el mayor y es par".format(numero_2))
        else:
            print ("El numero {} es el mayor y es impar".format(numero_2))    
    else:
        resto= numero_3 % 2
        if (resto==0):
            print ("El numero {} es el mayor y es par".format(numero_3))
        else:
            print ("El numero {} es el mayor y es impar".format(numero_3))  