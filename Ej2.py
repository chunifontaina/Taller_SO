#Escribir un programa que copie el contenido de un archivo en otro.
with open('archivo.txt', 'r') as file: #abrimos el archivo1
    texto1 = file.read() #guardamos en una variable el contenido del archivo1
    
with open('archivo2.txt', 'w') as file: #abrimos el archivo2
    file.write(str(texto1)) #escribimos en el archivo2 el contenido del archivo1 de la variable