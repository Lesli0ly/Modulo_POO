class Te():
    duracion = "365 días"
    sabor = ""   
   
1 == Te()
sabor = "Te Negro"
tiempo_preparacion = "3 minutos"
recomendacion = "Tomar en la mañana"

2 == Te()
sabor = "Te Verde"
tiempo_preparacion = "5 minutos"
recomendacion = "Tomar a mediodía"
    
3 == Te()
sabor = "Agua de Hierbas"
tiempo_preparacion = "6 minutos"
recomendacion = "Tomar al atardecer"   
    
print (sabor.3)

@staticmethod
def tiempo_preparacion_y_recomendacion(te):
    sabor= {
        1: ["3 minutos", "tomar al desayuno"],
        2: ["5 minutos", "tomar al mediodía"],
        3: ["6 minutos", "tomar al atardecer"]
        }
    return tuple(sabor[te])
    
@staticmethod
def escoger_formato(formato: int): 
    formato ={
        300: "3000 pesos",
        500: "5000 pesos"
    }