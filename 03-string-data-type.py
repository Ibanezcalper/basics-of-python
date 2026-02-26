#---Trabajando con el tipo de dato cadena---

#---Ejercicio 1: Presentar el tipo de datos cadena---
#Creamos una variable "myString" y guardamos texto
myString = "This is a string."

#Imprimimos el valor de la varibale "myString"
print(myString)

#Imprimimos el tipo de la varibale "myString"
print(type(myString))

#Imprimimos el valor de la varibale "myString", un texto y finalmente el tipo de la varibale "myString"
print(myString + " is of the data type " + str(type(myString)))

# ---Ejercicio 2: Trabajar con concatenación de cadenas---
#Asignamos valores a firstString y secondString
firstString = "water"
secondString = "fall"

#Usamos la concatenacion con "+" de los strings anteriores
thirdString = firstString + secondString

#Imprimimos la concatenacion
print(thirdString)

#---Ejercicio 3: Trabajar con cadenas de entrada---
#Input nos ayuda a almacenar el valor que se escriba en la consola
name = input("What is your name? ")

#Se imrpime el valor solicitado
print(name)

#---Ejercicio 4: Dar formato a las cadenas de salida---
#Input nos ayuda a almacenar el valor que se escriba en la consola
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

#Se imrpimen los valores solicitados
print("{}, you like a {} {}!".format(name,color,animal))