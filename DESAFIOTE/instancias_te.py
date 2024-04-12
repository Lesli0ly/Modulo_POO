from te import Te_artesanal

# Solicita al usuario que elija un tipo de te
tipo_te = int(input('''
    Por favor elija un tipo de té:
1. Té negro
2. Té verde
3. Agua de hierbas
    >>
'''))

# Solicita al usuario que elija un tamaño de te de dos opciones
formato = int(input('''
    Por favor elija un tamaño de té:
300 gramos
500 gramos
'''))

# Obtiene la preparacion recomendada y el precio del te elegido
sabor, tiempo, recomendacion = Te_artesanal.obt_preparacion_recomendacion(tipo_te)
precio = Te_artesanal.obt_precio_formato(formato)

# Imprime en interpolacion el resumen del pedido
print(f'''
    Detalles del pedido:
a. Sabor del té: {sabor}.
b. Tamaño del té: {formato} gramos.
c. Precio: ${precio}.
d. Tiempo de preparación recomendado: {tiempo}.
e. Recomendación: {recomendacion}.
''')