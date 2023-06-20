cadena1 = "aaaa"
cadena2 = "bienvenido"

#comvierte a mayuscula

Mayuscula = cadena1.upper ()

#convierte a minuscula

Minuscula = cadena1.lower ()

#primera letra en mayuscula

primera_letra_mayuscula = cadena1.capitalize

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1

busqueda_find = cadena1.find ("a")

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion

busqueda_index = cadena1.index ("a")

#si es numerico nos devuelve true, sino devuelve falso
es_numerico = cadena1.isnumeric ()

#si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha ()

print (es_alfanumerico)