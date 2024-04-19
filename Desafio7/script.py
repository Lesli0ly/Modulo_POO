from usuario import Usuario
import json
from datetime import datetime

#1:Lectura del archivo usuarios.txt
with open('Desafio7/usuarios.txt') as usuarios:
    linea = usuarios.readline()
    #7: variable de tipo lista para almacenar los objetos
    lista_objetos_usuarios = []
    
    #9: agregar en un ciclo
    while linea:
    
        #paso3: controlar la excepción
        try:
            
            #2: transformar el texto en json
            usuario_dicc = json.loads(linea)
            #print("usuario_dicc", usuario_dicc)
            #usuario_dicc {'nombre': 'Page', 'apellido': 'Stappard', 'email': }
    
            #6:Crear instancia de usuario
            usuario = Usuario (
                            usuario_dicc['nombre'],
                            usuario_dicc['apellido'],
                            usuario_dicc['email'],
                            usuario_dicc['genero'],
                            )
            lista_objetos_usuarios.append(usuario)
    
        except Exception as error:
            #4: imprimir el error
            print(f"el error es:", error)
            #5:Guardar el error en un log 
            now = datetime.now()
            with open(f"{now.strftime('%Y-%m-%d')}_error.log", 'a+') as log:
                print(log)
            
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {error}\n")
                #log.write(f"Error: {error}\n")

        finally:
            #8: posicionar en la siguiente linea
            linea = usuarios.readline()        
print("")
print("Contenido de la lista", lista_objetos_usuarios)