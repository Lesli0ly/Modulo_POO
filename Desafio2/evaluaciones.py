from pizza import Pizza
from ingredientes import Pizza

# Solicita al usuario que elija un tipo de masa
masa = int(input('''
    Por favor elija un tipo de masa:
1. Masa Tradicional
2. Masa Delgada
'''))

# Solicita al usuario que elija ingredientes vegetales
ingredientes_veg = int(input('''
    Por favor elija dos ingredientes vegetales:
1. Tomate
2. Champiñones
3. Aceitunas
'''))

# Solicita al usuario que elija el ingrediente proteico
ingredientes_pro = int(input('''
    Por favor elija dos ingredientes vegetales:
1. Pollo
2. Vacuno
3. Carne Vegetal
'''))

# Imprime en interpolacion el resumen del pedido
print(f'''
    Resumen del pedido:
a. Tipo de masa: {masa}.
b. Tamaño de la pizza: {Pizza.tamaño}
c. Precio: ${Pizza.precio}.
d. Ingredientes vegetales {ingredientes_veg}.
e. Ingredientes Proteicos: {ingredientes_pro}.
''')