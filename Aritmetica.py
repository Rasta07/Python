class Aritmetica:
   """
    El nombre de este tipo de comentario es : Docstring
    esto es documentaciòn de la clase en python
    Vammos a hacer en esta clase algunas operaciones de : suma, resta, multiplicacion y mas
    """

   def __init__(self, OperandoA, OperandoB):
       self.OperandoA = OperandoA
       self.OperandoB = OperandoB

# Metodo para sumar
   def sumar(self):
        return self.OperandoA + self.OperandoB

   def restar(self):
       return self.OperandoA - self.OperandoB

   def multiplicar(self):
       return self.OperandoA * self.OperandoB

   def dividir(self):
       return self.OperandoA / self.OperandoB

aritmetica1 = Aritmetica(7,9) # Le pasamos los argumentos para los operandos
print(f" La suma de los numeros es: {aritmetica1.sumar()}")
print(f" La resta de los numeros es: {aritmetica1.restar()}")
print(f" La multiplicación de los números es: {aritmetica1.multiplicar()}")
print(f" La división de los numeros es: {aritmetica1.dividir():.2f}")





