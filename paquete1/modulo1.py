class Persona:
    def __init__(self, nombre, edad, intereses):
        self.nombre = nombre
        self.edad = edad
        self.intereses = intereses

class Cliente(Persona):
    def __init__(self, nombre, edad, intereses, usuario, email, carrito=None):
        super().__init__(nombre, edad, intereses)
        self.usuario = usuario
        self.email = email
        self.carrito = carrito if carrito is not None else []


    def __str__(self):
        return f"¡Se ha creado el cliente '{self.nombre}' con éxito!"

    def agregar_producto(self, producto, tienda, mensaje):
        print("----------------------------------------")
        print(f"{mensaje}: {producto} en {tienda}")
        print("----------------------------------------")
        self.carrito.append((producto, tienda))

    def comprar(self, producto, tienda):
        self.agregar_producto(producto, tienda, "Producto comprado con éxito!")

    def añadir_carrito(self, producto, tienda):
        self.agregar_producto(producto, tienda, "Producto añadido al carrito")

    def remover_carrito(self, producto, tienda):
        carro = (producto, tienda)
        if carro in self.carrito:
            self.carrito.remove(carro)
            print("----------------------------------------")
            print(f"El producto {producto} ha sido eliminado del carrito")
            print("----------------------------------------")
        else:
            print("----------------------------------------")
            print("¡El producto no se encontró en el carrito!")
            print("----------------------------------------")

    def ver_carrito(self):
        if not self.carrito:
            print("El carrito está vacío.")
        else:
            print("----------------------------------------")
            for producto, tienda in self.carrito:
                print(f"Tiene estos productos: {producto} de la {tienda}, en el carrito.")
                print("----------------------------------------")