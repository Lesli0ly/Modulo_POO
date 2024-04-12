class Usuario():#pascal case
    nombre = "Julio"#atributo de la clase
    
julio = Usuario() #se crea una instancia de una clase u objeto
print(julio.nombre)

camilo = Usuario()
print(camilo.nombre)#imprime Julio

camilo.nombre = "Camilo"
print(camilo.nombre)
print(julio.nombre)