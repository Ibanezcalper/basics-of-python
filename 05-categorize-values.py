#--- Clasificación de valores ---
#--- Ejercicio 1: Crear una lista de varios tipos

# Definimos una lista de varios tipos
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
# Usamos el ciclo "for"  para recorrer cada elemento de la lista e imprimir el tipo de dato en ella
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))

