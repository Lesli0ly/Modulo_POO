#Definición de clase (molde o maqueta)
class Pelota():#Los objetos se escriben con mayúscula
    #atributos
    #pass (sin atributos ni métodos)
    forma="redonda"#cualquier tipo de dato, puede ir en el atributo, 
    #la forma de escribir en "snake_case". El atributo es considerado como 
    #una variable
#Dentro de las clases se pueden crear métodos, al igual que una función es la encargada de realizar una acción.  
#Instancia de una clase => Crear un objeto a partir de una clase
pelota_de_andy = Pelota()

print(pelota_de_andy.forma)
    
"""Ejercicio Guiado => Definir la clase medicamento"""

#definición de clase
class Medicamento():
    #atributos
    descuento = 0.05
    IVA = 0.18
    
Paracetamol = Medicamento()