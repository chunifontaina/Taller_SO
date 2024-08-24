#Escribir un programa que cuente la cantidad de líneas en un archivo.
with open('archivo.txt', 'r') as file: #abrimos el archivo
    lines = file.readlines() #leemos las lineas y las guardamos en una variable
    cantidad = len(lines) #leemos la cantidad de lineas
    print('Tiene ', cantidad, ' lineas')