class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial_compras = []  #una característica más que no le pasamos a traves del constructor y será una lista vacía

    def actualizar_informacion(self, direccion, telefono):     # Método propio de Cliente
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono
    
    def registrar_compra(self, compra):   # Método propio de Cliente
        self.historial_compras.append(compra)

    def mostrar_informacion(self):
        return f"Cliente: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"
    
  