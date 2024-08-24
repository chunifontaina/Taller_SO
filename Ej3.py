#Escribir un programa que, dados dos archivos, combine cada línea del primer archivo con la línea correspondiente del segundo. Es decir, concatenar la primera línea de ambos, luego la segunda, luego la tercera, etc. El resultado debe almacenarse en el segundo archivo.
with open('archivo.txt', 'r') as file: #abrimos el archivo1
    lines = file.readlines() #leemos las lineas y las guardamos en una variable

with open('archivo2.txt', 'r') as file: #abrimos el archivo2
    lines2 = file.readlines() #leemos las lineas y las guardamos en una variable

with open('archivo3.txt', 'w') as file: #abrimos el archivo3
    if len(lines) >= len(lines2): #si la cantidad de lineas del archivo1 es mayor o igual a la cantidad de lineas del archivo2
        for i in range(len(lines)): #recorremos las lineas del archivo1
            if i < len(lines2): #si existe un indice i en la lista de lineas del archivo2
                file.write(lines[i] + lines2[i] + '\n') #escribimos en el archivo3 la linea del archivo1 y del archivo2 concatenadas
            else: #si no existe un indice i en la lista de lineas del archivo2
                file.write(lines[i] + '\n') #escribimos solo la linea del archivo1
    else: #si la cantidad de lineas del archivo1 es menor a la cantidad de lineas del archivo2
        for i in range(len(lines2)): #recorremos las lineas del archivo2
            if i < len(lines): #si existe un indice i en la lista de lineas del archivo1
                file.write(lines[i] + lines2[i] + '\n') #escribimos en el archivo3 la linea del archivo1 y del archivo2 concatenadas
            else: #si no existe un indice i en la lista de lineas del archivo1
                file.write(lines2[i] + '\n') #escribimos solo la linea del archivo2