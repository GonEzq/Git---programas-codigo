#1. Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.

print ("Ingrese la longitud de los lados de un triangulo")
lado_1= float(input("Ingrese el lado 1: "))
lado_2= float(input("Ingrese el lado 2: "))
lado_3= float(input("Ingrese el lado 3: "))

if (lado_1 == lado_2 ):
    if (lado_1==lado_3):
        print("El triangulo es equilatero")
    else:
        print ("El triangulo es isosceles")
    
elif(lado_2==lado_3):
    print("El triangulo es isosceles")
elif(lado_1==lado_3):
    print("El triangulo es isosceles")    
else:
    print ("El triangulo es escaleno")   