#Definicion de la clase 'Producto'
class Producto:
    #Constructor de la clase 'Producto'
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre  #Inicializacion de los atributos privados nombre, precio y stock
        self.__precio = precio  
        self.__stock = (
            stock if stock > 0 else 0
        )  #Cantidad de unidades disponibles en el stock

    #Metodo 'getter' para el atributo privado nombre, precio y stock
    @property  
    def nombre(self):
        return self.__nombre  #Devuelve el nombre del producto

    @property
    def precio(self):
        return self.__precio  #Devuelve el precio del producto

    @property
    def stock(self):
        return self.__stock  #Devuelve la cantidad de unidades disponibles en el stock

    
    #Método 'setter' para el atributo privado stock
    @stock.setter
    def stock(self, stock):
        self.__stock = (
            stock if stock > 0 else 0
        )  #Actualiza la cantidad de unidades disponibles en el stock. Se establece como 0 si se escribe un valor negativo

    #Método especial para sumar el stock de dos productos
    def __add__(self, other):
        return (
            self.stock + other.stock
        )  # Retorna la suma de las cantidades de stock de dos productos

    #Método especial para restar el stock de dos productos
    def __sub__(self, other):
        return (
            self.stock - other.stock
        )  #Retorna la diferencia de las cantidades de stock de dos productos

    #Método especial para comparar la igualdad de dos productos por nombre
    def __eq__(self, other):
        return (
            self.nombre == other.nombre
        )  #Retorna True si los nombres de los productos son iguales, False en caso contrario