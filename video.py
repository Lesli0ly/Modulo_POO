import os

archivos = os.listdir()
for i in archivos:
    print(archivos)

lista = [1,2,3, "Hola", "Adiós"]
#Bucle for, recorrer elementos
for i in lista:
    print(i)
#Bucle while, para generar un bucle y termine bajo cierta condicion

contador = 0
while contador <= 10:
     contador +=1
     print("La variable contador en esta vuelta vale ", contador)
     

#funciones: para agrupar codigo de manera estructurada
def saludo():
    print ("Hola estoy dentro de la función saludo")
    print("Esto es todo")

saludo()

def despedida():
    print("Adiós!!")
    print("Hasta la proxima!!")
    
despedida()

Sentencias condicionales