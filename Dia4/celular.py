class Celular():
    def __init__(self, tamanio = 0):
        self.tamanio = tamanio
        
android = Celular(16)
iphone = Celular(16)

print(android)
print(iphone)
print (android == iphone)

windowp = android
print(windowp)

        