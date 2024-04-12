class Pelota():
    forma="redondeada"
    posiciones = [3,0,2,1,0]
    
#Método estático (se puede llamar directamente desde la clase, sin que se requiera crear una instancia)
#No se pueden modificar los atributos, que estuvieran definidos en la clase
    @staticmethod #decorador, se escribe en la línea anterior a la definición de un método
    def crear_rebote():
        posiciones = [5,0,4,0,3,0,2,0,1,0]
        return posiciones

    @staticmethod
    def imprimir_posiciones():
#Pelota.crear_rebote()
# #print(Pelota.posiciones):