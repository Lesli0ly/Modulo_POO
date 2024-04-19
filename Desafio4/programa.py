from tienda import Tienda, Restaurante, Supermercado, Farmacia
from producto import Producto

#Solicitar al usuario el tipo de tienda que desea agregar
tipo = int(
    input(
        "Por favor, ingrese el tipo de tienda que desea agregar:\n"
        "1. Restaurante\n"
        "2. Supermercado\n"
        "3. Farmacia\n"
    )
)
nombre = input("\nIngrese el nombre de la tienda que desea agregar:\n")
delivery = int(input("\nIngrese el precio del servicio de entrega:\n"))

# Crear una instancia de la tienda correspondiente segun el tipo de tienda ingresado
if tipo == 2:
    tienda = Supermercado(nombre, delivery)
elif tipo == 3:
    tienda = Farmacia(nombre, delivery)
else:
    tienda = Restaurante(nombre, delivery)

opcion = 1

#Permitir al usuario agregar productos a la tienda
while opcion == 1:
    print("..........................\n")
    nombre_producto = input("\nIngrese el nombre del producto que desea agregar:\n")
    
    print("..........................\n")
    precio = int(input("\nIngrese el precio del producto:\n"))
    
    print("..........................\n")
    stock = int(input("\nIngrese el stock del producto:\n"))
    
    print("..........................\n")
    tienda.ingresar_producto(nombre_producto, precio, stock)
    
    opcion = int(input("\n¿Desea agregar otro producto?\n" 
                       "1. Sí\n"
                       "2. No\n"))

# Menu de opciones para interactuar con los productos de la tienda
opcion_productos = int(
    input(
        "\nIndique qué desea realizar:\n"
        "1. Listar productos disponibles en la tienda\n"
        "2. Realizar una venta de producto\n"
        "3. Salir\n"
    )
)

while opcion_productos in [1, 2]:
    if opcion_productos == 1:
        print(tienda.listar_productos())#Mostrar la lista de productos disponibles en la tienda
    elif opcion_productos == 2:
        
        #Permitir al usuario realizar una venta de producto
        nombre_producto = input("\nIngrese el nombre del producto que desea vender:\n")
        
        cantidad = int(input("\nIngrese la cantidad que desea comprar:\n"))
        
        tienda.realizar_venta(nombre_producto, cantidad)

    # Solicitar al usuario otra opcion
    opcion_productos = int(
        input(
            "\nIndique qué desea hacer:\n"
            "1. Listar productos disponibles en la tienda\n"
            "2. Realizar una venta de producto\n"
            "3. Salir\n"
        )
    )