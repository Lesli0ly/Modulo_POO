class Pizza:
    precio = 10000
    tamaño = "Familiar"
    
    def __init__(self, ingredientes_veg, ingredientes_pro, masa):
        self.ingredientes_veg = ingredientes_veg
        self.ingredientes_pro = ingredientes_pro
        self.masa = masa



def armar_pizza (masa):
    masa = {
        1: "Tradicional",
        2: "Delgada"
    }

def armar_pizza (ingredientes_veg):
    ingredientes_veg = {
        1: "Tomate",
        2: "Champiñones",
        3: "Aceitunas"
    }

def armar_pizza (ingredientes_pro):
    ingredientes_pro = {
        1: "Pollo",
        2: "Vacuno",
        3: "Carne Vegetal"
    }
    