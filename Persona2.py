class Persona2:
    def __init__(self,nombre,apellido,edad): # esta encapsulado
        self._nombre= nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre}{self._apellido}{self._edad}")

    @property #decorador
    def nombre(self): #Metodo Getter
        print("Estamos utilizando el método get")
        return self._nombre

    @nombre.setter
    def nombre(self,nombre): #Metodo Setter
        print("Estamos utilizando el método set")
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        self._apellido= apellido

    @property
    def edad(self):
        return(self)._edad

    @edad.setter
    def edad(self,edad):
        self._edad= edad
    def __del__(self):
        print(f"Persona2 : {self._nombre}{self._apellido}{self._edad}")
if __name__ == "__main__":


    persona1 = Persona2("Fernando "," Barrionuevo ",30)
    print(persona1.nombre) # Llamamos al método getter
    persona1.nombre= " Martín " #Llamamos el método setter
    print(persona1.nombre) #Otra vez con el méttodo getter
    print(persona1.mostrar_detalles()) #Llamamos  el metodo mostrar detalles
    #Atributo read-only (solo lectura seeria la edad porque no tiene el metodo set)
    print(persona1.edad)

    # Tarea crear tres objetos mas, utilizando los metodos getter and setter
    #para modificar,y mostrar los cambios con el metodo mostrar_detalles

    persona2= Persona2("Valen","Marquez",25)
    persona2.nombre = "Valentina "
    persona2.apellido= "Marques "
    persona2.edad= 27
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalles())



    persona3= Persona2("Euge","Quevedo",24)
    persona3.nombre= "Eugenia "
    persona3.apellido= "Quevedo "
    persona3.edad= 30
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalles())

    persona4= Persona2("Lucre","Torrez",30)
    persona3.nombre= "Lucresia "
    persona3.apellido= "Torres "
    persona3.edad= 32
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    print(persona3.mostrar_detalles())

