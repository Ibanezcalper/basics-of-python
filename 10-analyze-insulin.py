import re #Para leer expresiones regulares

# Abrimos el archivo de texto
with open("preproinsulin-seq.txt", "r") as f:
    #Leemos todo el contenido del archivo
    raw_data = f.read()

# Vamos a eliminar "ORIGIN"
clean_data = re.sub(r"\bORIGIN\b", "", raw_data, flags=re.IGNORECASE)

# Vamos a eliminar terminador de registro "//"
clean_data.replace("//","")

# Vamos a eliminar cualquier cosa que no sea letra
clean_data = re.sub(r"[^A-Za-z]", "", clean_data)

# Convertimos todo a minusculas
clean_data = clean_data.lower()

#--- Contar el numero de caracteres de preproinsulin
# Abrir nuevamente el archivo

with open("preproinsulin-seq.txt", "w") as f:
    #limpiamos el archivo
    f.write(clean_data)

# Calculamos la longitud de preproinsulin    
print("Longitud preproinsulin = ", len(clean_data))

# Si la secuencia no tiene 110 caracteres nos salimos del programa
if len(clean_data) != 110:
    print("Error!, la secuencia no tiene 110 caracteres")
    exit()
    
    
# Extramos los primeros 24 caracteres
lsinsulin = clean_data[0:24]

# Extramos del caracter 25 al 54
binsulin = clean_data[24:54]

# Extramos del caracter 55 al 89
cinsulin = clean_data[54:89]

# Extramos del caracter 90 al 110
ainsulin = clean_data[89:110]

# Creamos diferentes archivos
with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(lsinsulin)
    
with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(binsulin)
    
with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(cinsulin)
    
with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(ainsulin)

# Verifamos el tamaño de los caracteres
print("lsinsulin = ", len(lsinsulin))
print("binsulin = ", len(binsulin))
print("cinsulin = ", len(cinsulin))
print("ainsulin = ", len(ainsulin))

insulin = binsulin + ainsulin

# Total de insulina procesada
print("Insulina procesada = ", len(insulin))

# Secuencia de la insulina
print("Secuencia de la insulina = ", insulin)