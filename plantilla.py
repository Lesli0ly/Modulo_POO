class Superficie():
    def __init__(self):
        self.__resistencia = 2

@property
def resistencia(self):
    return self.__resistencia

class Pelota():
    def rebotar(self, altura: float):
    
# Se instancia la clase que colabora con Pelota
    s = Superficie()
    rebotes = []
    while altura > 0:
        rebotes.append(altura)
        rebotes.append(0)
# La instancia de Superficie colabora con Pelota para rebotar
altura //= s.resistencia
return rebotes
p = Pelota()
# Salida: [10, 0, 5, 0, 2, 0, 1, 0]
print(p.rebotar(10))

class Material():
    def __init__(self, nombre: str, duracion: str, textura: str):
        self.nombre = nombre
        self.duracion = duracion
        self.textura = textura

class Pelota():
    def __init__(self, tamanio: int, color: str, material: Material):
        self.tamanio = tamanio
        self.color = color

# La pelota tiene un material
self.material = material

# El material existe en forma independiente de la pelota
m = Material("Plástico", "Corta", "Lisa")
p = Pelota(16, "Amarillo", m)

# Salida: <class '__main__.Material'>
print(type(p.material))

# Salida: Plástico
print(p.material.nombre)

from abc import ABC, abstractmethod

class Material(ABC):
    
@abstractmethod
def romper(self):
    pass

class MaterialPlastico(Material):
    nombre = "Plástico"
    duracion = "Corta"

def __init__(self, textura: str):
    self.textura = textura
    
def romper(self):
    pass
class Pelota():
    def __init__(self, tamanio: int, color: str, textura: str):
        self.tamanio = tamanio
        self.color = color
        self.textura = textura
        
# La pelota está compuesta por un componente material
self.material = MaterialPlastico(self.textura)
p = Pelota(16, "Amarillo", "Lisa")
# Salida: Plástico
print(p.material.nombre)