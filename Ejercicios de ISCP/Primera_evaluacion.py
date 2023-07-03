print("convertir un numero a los siguientes medidas")
def conversion(centimetros):

    
       
    pulgadas = centimetros * 0.393701
    metros = centimetros * 0.01
    milimetros = centimetros * 10
    return centimetros,metros,milimetros,pulgadas

covertir = float(input("Ingresar numero: ")) 

metros,centimetros,milimetros,pulgadas = conversion (covertir)

print (f'pulgadas: {pulgadas} in\nMetros: {metros} m \nmilimetros: {milimetros} mm \ncentimetros {centimetros}')

