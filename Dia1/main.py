from pelota import Pelota
from medicamento import Medicamento

#Instancia
pelota_de_andy = Pelota()
print(pelota_de_andy.forma)
print(pelota_de_andy.posiciones)
print(pelota_de_andy.crear_rebote())

#Invocación de Método Estático
print(Pelota.crear_rebote())
Pelota.imprimir_posiciones()
print(Pelota.posiciones)
print("")
#Llamar a método NO ESTÁTICO
#Pelota.rebotar()#TypeError: Pelota.rebotar()missing 1 required positional
pelota_de_andy.rebotar()

print(Pelota.posiciones, Pelota.forma)
print(pelota_de_andy.posiciones, pelota_de_andy.forma)

pelota_de_tenis = Pelota()
print(pelota_de_tenis.posiciones, pelota_de_tenis.forma)


#sobrecarga -> Modificar el comportamiento del método
"""def __str__(self):
    return f"forma: {self.forma}, color: {self.color}, material: {self.material}"
()
print(pelota_futbol)"""
