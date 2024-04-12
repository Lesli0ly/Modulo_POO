#se importa para crear una clase abstracta
from abc import ABC, abstractmethod

class Pelota(ABC):
    #definicion del método, no hay ninguna lógica, 
    # solo la definición de un método, no tiene implementación (no se le agregó contenido o desarrollo)
    @abstractmethod
    def rebotar(self, altura: int):
        pass
#TypeError: can't instantiate abstract class Pelota without an implementation for abstract method 
#pelotita = Pelota() # NO SE PUEDE INSTANCIAR UNA CLASE ABSTRACTA   
pelotita = Pelota() 

class PelotaDeJuguete(Pelota):
    def __init__(self, color:str):
        self.rebotes=[]
    #__ para definir atributo privado
    self._color = color
    
    #ES OBLIGATORIO, sino arroja error, implementar el metodo que es abstracto
    def rebotar(self, altura: int): 
        print(altura)  
    
    #metodo get --> traer u obtener información de un atributo
    @property
    def color(self):
        return self._color
    
    #metodo set -> asigna el valor al atributo
    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color        
        

pelotita = PelotaDeJuguete("amarilla")
print("llamado al get de color",pelotita.color)

pelotita._color = "verde"#no afecta el valor del atributo
print("llamado al get de color",pelotita.color)

#pelotita.color("azul") no se debe tratar como metodo
pelotita.color = "azul" # set 
print("llamado al get de color",pelotita.color)#get

pelotita.