class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad, con
    un método calcular volumen que tendra la formula:
    volumen= ancho * altura * profundidad
    que el usuario ingrese los valores.
    """
    def __init__(self, ancho,altura,profundidad):
        self.ancho= ancho
        self.altura=altura
        self.profundidad=profundidad


    def Calcular_Volumen(self):
        return self.ancho * self.altura * self.profundidad

ancho= int(input("Digite el ancho del cubo: "))
altura= int(input("Digite la altura del cubo: "))
profundidad= int(input("Digite la profundidad del cubo: "))

Cubo1 = Cubo(ancho, altura, profundidad)
print(f"el volumen del cubo es : {Cubo1.Calcular_Volumen()}")
