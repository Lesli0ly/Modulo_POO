from medicamento import Medicamento


precio = int(input("Ingrese un precio a validar: "))
es_valido = Medicamento.validar_mayor_a_cero(precio)


if es_valido:
    print("El precio ingresado es válido")
else: 
    print("El precio ingresado no es válido")
    

# Instancia clase medicamento
paracetamol = Medicamento()
print(paracetamol.IVA)
print(paracetamol.descuento)

aspirina = Medicamento()
print(aspirina.IVA)
print(aspirina.descuento)

if paracetamol.descuento == aspirina.descuento and paracetamol.IVA == aspirina.IVA:
    print("Todos los valores son iguales en las instancias")
    print(paracetamol.IVA, aspirina.IVA)
    print(paracetamol.descuento, aspirina.descuento)
    
print(aspirina.validar_mayor_a_cero(0))