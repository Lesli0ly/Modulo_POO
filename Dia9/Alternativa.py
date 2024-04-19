class Alternativa:
    
    alternativas = [
	{
	"contenido": "contenidos",
	"ayuda": "ayudita "
	},
	{
	"contenido": "contenidos",
	"ayuda": "ayudita "
	},
	{
	"contenido": "contenidos",
	"ayuda": "ayudita "
	}
]   
    def mostrar_alternativa(self):
        print(self.contenido)
        if self.ayuda:
            print("ayuda!!", self.ayuda)

if __name__=="__main__":
    dicc = {}