
#2. Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:
# • Contado (1): se aplica un descuento del 10% al importe
# • Tarjeta (2): se aplica un interés de 10%
# • Débito (3): se aplica un descuento del 5%
# Mostrar el importe, el descuento o interés y el importe total.

importe= int(input("Ingrese el importe ha pagar: $"))
print ("Metodo de pago")
print("1- Contado")
print("2- Tarjeta")
print("3- Debito")
opcion=int(input("Ingrese la opcion necesaria: "))

if(opcion==1):
    print("Su importe es: ${:.2f} ".format(importe) )
    print("Descuento ${:.2f} ".format(importe*0.1))
    print ("Su importe total es: ${:.2f}" .format(importe*0.9))

elif(opcion==2):
    print("Su importe es: ${:.2f} ".format(importe) )
    print("Interes ${:.2f} ".format(importe*0.1))
    print ("Su importe total es: ${:.2f}" .format(importe*1.1))    

elif(opcion==3):
    print("Su importe es: ${:.2f} ".format(importe) )
    print("Descuento ${:.2f} ".format(importe*0.05))
    print ("Su importe total es: ${:.2f}" .format(importe*0.95))    

else:
    print("Opcion INCORRECTA")    