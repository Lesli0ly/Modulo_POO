

class Pregunta():
    def __init__(self, enunciado: str, ayuda: str, requerido: bool, alternativas: list):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerido = requerido
        
        #Considerar que las alternativas son entregadas como una lista de dicionarios
        self.__alternativas = []
        
    
    def mostrar_pregunta(self, ):
        pass

alternativas = [
{
    "contenido": "contenidos1",
    "ayuda": "ayudita1"
    },
{
    "contenido": "contenidos2",
    "ayuda": "ayudita2"
    },
{
    "contenido": "contenidos3",
    "ayuda": "ayudita3"
    },
]

for dicc in alternativas:
    print (dicc)