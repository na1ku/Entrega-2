from paquete1.modulo1 import Cliente

cliente1 = Cliente("Nicolas", 29, "Juegos, Comics y Mangas", "Naiku", "mail@mail.com")

print(cliente1)
cliente1.añadir_carrito("Comic", "Tiendamia")
cliente1.comprar("Playstation 5", "Sony")
cliente1.ver_carrito()
cliente1.remover_carrito("Comic", "Tiendamia")
