from te import instancias

sabor = int(input("""
    Ingrese el sabor del Té escogido:
1.- Té negro
2.- Té verde
3.- Agua de hierbas"""))

formato = int(input(""" Escoja uno de los dos formatos, en gramos:
                    300
                    500"""))
                    
                    
print(f"""
    Detalle del Pedido:\n
    Sabor del tipo de té: {sabor}
    Formato:{formato}
    Tiempo de preparación:
    Recomendación:
         
      """)