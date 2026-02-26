#Se va a crear un validador para saber si podemos o no podemos entrar a una fiesta, es importante agregar que para entrar a la fiesta debes ser mayor de edad
#Se crea la variable edad y en ella se va a guardar lo que diga el usuario
#Vamos a comparar si la edad es mayor o igual a 18
edad = input("Escriba su edad: ")

#convertimos la variable entrada debido a que cuando se escribe por consola el valor que se guarda es el de un texto
edad = int(edad)

#Vamos a conmparar si la edad es mayor o igual a 18 años
if edad >= 18:
    #Imprime que lo deja entrar
    print("Puede entrar")
else:
    #Si no se cumple la condición de ser mayor de 18 años, imprime "no puedo entrar"
    print("No puede entrar")
    
#Ahora se va a validar si la persona es mayor de edad y además tiene más de $600
#Se crea la variable edad y en ella se guarda lo que escriba el usuario
edad = input("Escriba su edad: ")

#convertimos la variable entrada debido a que cuando se escribe por consola el valor que se guarda es el de un texto
edad = int(edad)

#Se crea la variable dinero y en ella se guarda lo que escriba el usuario
dinero = input("Escriba su ccantidad de dinero: ")

#convertimos la variable entrada debido a que cuando se escribe por consola el valor que se guarda es el de un texto
dinero = int(dinero)

#Vamos a conmparar si la edad es mayor o igual a 18 años
if edad >= 18:
    #Verificamos si cuenta con el dinero
    if  dinero >= 600:
        #Imprime que lo deja entrar
        print("Puedo entrar")
    else:
        #Como no tiene el dinero no puede entrar
        print("No puede entrar")
else:
    #Como no tiene la edad no puede entrar:
    print("No puede entrar")
    
    
#----------------Versión 2-------------------

#Vamos a conmparar si la edad es mayor o igual a 18 años
if edad >= 18 and dinero >= 600:
    #Imprime que lo deja entrar
    print("v2 Puede entrar")
else:
    #Como no tiene la edad no puede entrar:
    print("v2 No puede entrar")