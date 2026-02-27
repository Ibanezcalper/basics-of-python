# --- Uso de funciones para implementar un cifrado César ---
# Información general sobre el laboratorio
#En programación, una función es una sección con nombre dentro de un programa 
#que realiza una tarea específica. Python tiene funciones integradas como print() 
# proporcionadas por el mismo lenguaje. Además, puede utilizar funciones 
# proporcionadas por otros desarrolladores a través de la instrucción import. 
# Por ejemplo, puede utilizar import math si desea utilizar la función math.floor(). 
# En Python, puede crear sus propias funciones, denominadas funciones definidas por el usuario.

# Para continuar el debate sobre las funciones definidas por el usuario, 
# escribirá un programa para implementar un cifrado César, que es un
# método sencillo de cifrado. El cifrado César toma las letras de un mensaje y
# desplaza cada letra a lo largo del alfabeto un número determinado de posiciones.

# En este laboratorio, deberá realizar lo siguiente:

    # crear funciones definidas por el usuario
    # utilizar varias funciones para implementar un programa de cifrado César
    
# Una función recibe parametros o variables para realizar una tarea especifica


#--- Ejercicio 1: Creación de una función definida por el usuario ---
# La idea es “mover” cada letra del mensaje un número de posiciones (la clave).
# Por ejemplo, si la clave es 3: A -> D, B -> E, C -> F, etc.

# Esta función recibe un alfabeto (un texto) y lo pega consigo mismo.
# Lo hacemos para poder “movernos” hacia adelante sin quedarnos sin letras.
# Ejemplo: "ABC" se vuelve "ABCABC".
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
    
#--- Ejercicio 2: Cifrado de un mensaje ---  
# Esta función le pide al usuario que escriba un mensaje.
# Lo que el usuario escriba se guarda y luego se devuelve.
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
    

#--- Ejercicio 3: Obtención de una clave de cifrado ---

# Esta función le pide al usuario una clave.
# La clave es un número del 1 al 25 que indica cuánto se moverán las letras.
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount
    
    
# --- Ejercicio 4: Cifrado de un mensaje ---
# Esta función hace el trabajo de encriptar moviendo la letra n posiciones a la derecha.

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
    
    
# --- Ejercicio 5: Descifrado de un mensaje ---
# Esta función hace el trabajo de encriptar moviendo la letra n posiciones
# a la izquierda a partir del mensaje encriptado.

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    

#--- Ejercicio 6: Creación de una función principal ---
# Esta función hace el trabajo de encriptar.
# Recorre el mensaje letra por letra, busca cada letra en el alfabeto,
# le suma la clave para “moverla”, y va armando el mensaje encriptado.

def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    # Duplico el alfabeto para poder desplazar letras sin problemas
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    # Pido el mensaje al usuario
    myMessage = getMessage()
    print(myMessage)
    # Pido la clave al usuario
    myCipherKey = getCipherKey()
    print(myCipherKey)
    # Encripto el mensaje
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    # Desencripto el mensaje (para comprobar que vuelve al original)
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
runCaesarCipherProgram()