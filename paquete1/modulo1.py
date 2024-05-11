class Cliente:
    def __init__(self, nombre, apellido, edad, direccion, telefono, email, interes):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.interes = interes
        self.puntos = 0

    def comprar(self, producto, tienda):
        print(f"{self.nombre} ha comprado {producto} en {tienda}.")
        self.sumar_puntos(10)  # Añadir puntos por la compra

    def sumar_puntos(self, cantidad):
        self.puntos += cantidad

    def imprimir_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Email: {self.email}")
        print(f"Intereses: {self.interes}")
        print(f"Puntos acumulados: {self.puntos}")  # Mostrar los puntos acumulados

    def __str__(self):
        return f"Hola, soy el cliente {self.nombre} {self.apellido}, tengo {self.edad} años, mis datos son los siguientes:\nDirección: {self.direccion}\nTeléfono: {self.telefono}\nEmail: {self.email}\nPuntos acumulados: {self.puntos}"


