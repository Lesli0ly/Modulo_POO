from abc import ABC, abstractmethod # Importacion de la clase abstracta ABC y el decorador @abstractmethod del modulo abc.
from producto import Producto


#Definicion de la subclase abstracta 'Tienda' de la clase abstracta ABC.
class Tienda(ABC):
    #Metodo abstracto para ingresar un producto a la tienda.
    @abstractmethod
    def ingresar_producto(self, nombre: str, precio: int, stock: int):
        pass

    # Metodo abstracto para listar los productos disponibles en la tienda.
    @abstractmethod
    def listar_productos(self):
        pass

    #Metodo abstracto para realizar una venta de producto en la tienda.
    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass



class Restaurante(Tienda):#Definicion de la clase concreta 'Restaurante' de la clase abstracta 'Tienda'.
    tipo = "Restaurante"

    def __init__(self, nombre, delivery):#Constructor de la clase con parametros 'nombre' y 'delivery'.
        self.__nombre = nombre
        self.__delivery = delivery
        
        self.__productos = []#Inicializacion del atributo privado productos como una lista vacia.

    
    def ingresar_producto(self, nombre, precio, stock):#Metodo para ingresar un producto al restaurante.
        p = Producto(nombre, precio)
        
        #Filtrado de productos y correlación con los productos que ya estan ingresados en cada tienda
        encontrados = list(filter(lambda x: x == p, self.__productos))
        
        #Si no se encontraron productos iguales, se agrega el nuevo producto al final de la lista con 'append'
        if len(encontrados) == 0:
            self.__productos.append(p)

    
    def listar_productos(self):#Método para listar los productos disponibles en el restaurante.

        
        if len(self.__productos):#Verificar de si hay productos en la lista.
            retorno = " "
            # Iteracion sobre los productos para formar la cadena de retorno.
            for p in self.__productos:
                retorno += f"NOMBRE: {p.nombre}\t" + f"PRECIO: ${p.precio}\n\n"
            return retorno
        else:
            return "No hay productos para esta tienda"

    #Metodo para realizar una venta en el restaurante (sin realizar alguna acción).
    def realizar_venta(self, nombre_producto, cantidad):
        pass


#Definición de la clase concreta Farmacia que hereda de la clase abstracta Tienda.
class Farmacia(Tienda):
    #Definición del atributo de clase tipo.
    tipo = "Farmacia"

    #Constructor de la clase con parámetros nombre y delivery.
    def __init__(self, nombre, delivery):
        self.__nombre = nombre#Inicialización de atributos privados nombre y delivery.
        self.__delivery = delivery
        
        self.__productos = []#Inicialización del atributo privado productos como una lista vacía.

    #Método para ingresar un producto a la farmacia.
    def ingresar_producto(self, nombre: str, precio: int, stock: int):
        
        p = Producto(nombre, precio, stock)
        
        encontrados = list(filter(lambda x: x == p, self.__productos))#Filtrado de productos iguales al producto a ingresar.
        #Si no se encontraron productos iguales, se agrega el nuevo producto, con if y se actualiza con else.
        if len(encontrados) == 0:
            self.__productos.append(p)
        else:
            indice = self.__productos.index(p)
            self.__productos[indice].stock = p + self.__productos[indice]

    #Método para listar los productos existentes en la farmacia.
    def listar_productos(self):
        
        if len(self.__productos):#Verificación de si hay productos en la lista.
            retorno = " "
            
            for p in self.__productos:#Iteracion sobre los productos para formar la cadena de retorno.
                m = " "
                if p.precio > 15000:
                    m = "(Envío gratis al solicitar este producto)"
                retorno += f"NOMBRE: {p.nombre}\t" + f"PRECIO: ${p.precio}{m}\t"
            return retorno
        else:
            return "No hay productos para esta tienda"

    #Metodo para realizar una venta en la farmacia (sin implementar).
    def realizar_venta(self, nombre_producto, cantidad):
        pass


#Definicion de la clase concreta Supermercado que hereda de la clase abstracta Tienda.
class Supermercado(Tienda):
    #Definicion del atributo de clase tipo.
    tipo = "Supermercado"

    # Constructor de la clase con parametros nombre y delivery.
    def __init__(self, nombre: str, delivery: int):
        self.__nombre = nombre#Inicializacion de atributos privados nombre y costo_delivery.
        self.__delivery = delivery
        
        self.__productos = []#Inicializacion del atributo privado productos como una lista vacia.

    # Metodo para ingresar un producto al supermercado.
    def ingresar_producto(self, nombre, precio, stock):
        
        p = Producto(nombre, precio, stock)#Filtrado de productos iguales al producto a ingresar.
        encontrados = list(filter(lambda x: x == p, self.__productos))
        
        if len(encontrados) == 0:#Si no se encontraron productos iguales, se agrega el nuevo producto con append.
            self.__productos.append(p)
        else: #Si se encontro un producto igual, se actualiza su stock.
            indice = self.__productos.index(p)
            self.__productos[indice].stock = p + self.__productos[indice]

    #Metodo para listar los productos disponibles en el supermercado.
    def listar_productos(self):
        
        #Verificacion de si hay productos en la lista.
        if len(self.__productos):
            retorno = " "
            #Iteracion sobre los productos para formar la cadena de retorno.
            for p in self.__productos:
                m = " "
                if p.stock < 10:
                    m = "(Pocos productos disponibles)"
                retorno += (
                    f"NOMBRE: {p.nombre}\t"
                    + f"PRECIO: ${p.precio}\t"
                    + f"STOCK: {p.stock}{m}"
                )
            return retorno
        else:
            return "No hay productos para esta tienda"