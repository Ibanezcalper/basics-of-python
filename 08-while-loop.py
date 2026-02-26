#--- Trabajo con bucles ---
#--- Ejercicio 1: Trabajo con un bucle while ---
# Importamos la libreria random
import random

#informa al usuario del inicio del juego
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#--- Importación aleatoria y escritura de un bucle while ---
# Se genera un numero aleatio entre 1 y 10
number = random.randint(1,10)

#Monitorea si el usuario adivino el numero
isGuessRight = False

# Se crea la logica del juego
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))