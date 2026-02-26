#--- Trabajo con listas, tuplas y diccionarios---
#--- Ejercicio 1: Presentar el tipo de dato de lista---

#--- Definición de una lista---


myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# Acceso a una lista por posición
print(myFruitList[0]) # aaple
print(myFruitList[1]) # banana
print(myFruitList[2]) # cherry


#--- Modificación de los valores de una lista ---

myFruitList[2] = "orange"
print(myFruitList)


#--- Ejercicio 2: Presentar el tipo de dato de tupla ---
#--- Definición de Tupla ---
#--- Una tupla es similar a una lista, pero no se puede cambiar. 
#--- Un tipo de dato que no se puede cambiar después de su creación se conoce como inmutable. 
#--- Para definir una tupla, se utilizan paréntesis en lugar de corchetes ([]). ---

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#--- Acceso a una tupla por posición
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#--- Ejercicio 3: Presentar el tipo de dato de diccionario ---
#--- Definición de un diccionario ---
#--- Un diccionario es una lista cuyas posiciones tienen nombres asignados (claves). 
#--- Imagine que su lista muestra la fruta favorita de distintas personas.

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

# Acceso al diccionario por nombre
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
