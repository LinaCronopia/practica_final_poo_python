class Mascota:
    def __init__(self, nombre, edad, salud, precio):  # Constructor de mascota
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.precio = precio

    def actualizar_informacion(self, edad=None, salud=None, precio=None):  # Método de mascota
        if edad:
            self.edad = edad
        if salud:
            self.salud = salud
        if precio:
            self.precio = precio

    def mostrar_informacion(self):
        return f"Mascota: {self.nombre}, edad: {self.edad}, salud: {self.salud}, precio: {self.precio}"


# Dos clases que hereden de Mascota
class Perro(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, nivel_de_energia):
        super().__init__(nombre, edad, salud, precio)  # super() para poder pasarle al constructor de la clase padre, que hereda
        self.raza = raza
        self.nivel_de_energia = nivel_de_energia

    def mostrar_caracteristicas(self):  # Método propio de Perro
        return f"Raza: {self.raza}, Nivel de energía: {self.nivel_de_energia}"


class Gato(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, independencia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza  # raza podría estar en el constructor de Mascota porque es igual en Perro y Gato. (fines de aprendizaje)
        self.independencia = independencia

    def mostrar_caracteristicas(self):  # Método propio de Gato
        return f"Raza: {self.raza}, Independencia: {self.independencia}"
