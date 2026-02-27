#--- Creación de controladores de archivos y módulos para recuperar información sobre la insulina ---
#--- Información general sobre el laboratorio ---
# En este laboratorio, deberá realizar lo siguiente:

    # crear un módulo
    # abrir un archivo y cargar los datos JSON que contiene con
        # el uso del módulo integrado JSON de Python
    # analizar la estructura JSON para acceder a los datos de insulina
    # calcular el peso molecular aproximado de la insulina utilizando un 
    # código dado (similar al laboratorio Trabajo con la secuencia de cadena y
        # el peso numérico de la insulina en Python
        
#--- Ejercicio 1: Creación del archivo de datos de moléculas JSON ---
#--- Ejercicio 2: Creación del módulo controlador de archivos JSON ---

# Importo la librería json que me permite trabajar con archivos JSON
import json
import re

# Creo una función que recibe el nombre del archivo JSON
def readJsonFile(fileName):
    # Inicializo la variable data como vacía
    # Si algo falla, devolverá esto
    data = ""
    try:
        # Intento abrir el archivo que me pasaron como parámetro
        with open(fileName) as json_file:
            # json.load convierte el archivo JSON en un diccionario de Python
            data = json.load(json_file)
    except IOError:
    # Si ocurre un error al abrir el archivo, muestro este mensaje
        print("Could not read file")
        # Devuelvo los datos leídos (o vacío si falló)
    return data
    
# Continuamos en el archivo 14.1