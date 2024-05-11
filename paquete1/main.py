from modulo1 import Cliente
from modulo2 import leerData, guardar_data, registrar_usuario, mostrar_usuarios, login_usuario

def proceso_compra(usuario, sesiones):
    base_datos = leerData()  

    if usuario not in sesiones:
        print("Debes iniciar sesión primero.")
        return

    if not base_datos:
        print("No hay usuarios registrados. Por favor, regístrese antes de realizar una compra.")
        return

    if usuario not in base_datos:
        print("Usuario no encontrado. Por favor, inicie sesión nuevamente.")
        return

    nombre = base_datos[usuario].get("nombre")
    email = base_datos[usuario].get("email")
    intereses = base_datos[usuario].get("intereses")
    edad = base_datos[usuario].get("edad")
    pais = base_datos[usuario].get("pais", "Desconocido")

    cliente_actual = Cliente(nombre, edad, intereses, usuario, email)  # Eliminamos el argumento carrito

    while True:
        print("\n*** Menú de opciones ***")
        print("1. Comprar producto")
        print("2. Agregar producto al carrito")
        print("3. Remover producto del carrito")
        print("4. Ver carrito")
        print("5. Finalizar compra")
        print("6. Salir")
        opcion = input("¿Qué acción desea realizar? Ingrese el número correspondiente: ")

        if opcion == "1":
            print("\n*** Comprar producto ***")
            producto = input("Ingrese el producto que desea comprar: ")
            tienda = input("En qué tienda desea realizar la compra: ")
            cliente_actual.comprar(producto, tienda)
            base_datos[usuario]["productos"].append((producto, tienda))
            guardar_data(base_datos)
        elif opcion == "2":
            print("\n*** Agregar producto al carrito ***")
            producto = input("Ingrese el producto que desea añadir al carrito: ")
            tienda = input("En qué tienda desea añadir el producto al carrito: ")
            cliente_actual.añadir_carrito(producto, tienda)
            base_datos[usuario]["productos"].append((producto, tienda))
            guardar_data(base_datos)
        elif opcion == "3":
            print("\n*** Remover producto del carrito ***")
            if not base_datos[usuario]["productos"]:
                print("El carrito está vacío. No hay productos para remover.")
            else:
                producto = input("Ingrese el producto que desea eliminar del carrito: ")
                tienda = input("En qué tienda desea eliminar el producto del carrito: ")
                carro = (producto, tienda)
                if carro in base_datos[usuario]["productos"]:
                    cliente_actual.remover_carrito(producto, tienda)
                    base_datos[usuario]["productos"].remove((producto, tienda))
                    guardar_data(base_datos)
                else:
                    print("----------------------------------------")
                    print("¡El producto no se encontró en el carrito!")
                    print("----------------------------------------")
        elif opcion == "4":
            print("\n*** Ver carrito ***")
            cliente_actual.ver_carrito()
        elif opcion == "5":
            print("\n*** Finalizar compra ***")
            print("----------------------------------------")
            print(f"Muchas gracias por comprar, se ha enviado la factura detallada al e-mail: {cliente_actual.email}")
            print("----------------------------------------")
            break
        elif opcion == "6":
            print("\nSaliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def menu_principal():
    print("\n*** Menú principal ***")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Mostrar usuarios")
    print("4. Comprar productos")
    print("5. Salir")
    opcion = input("Seleccione una opción ingresando el número correspondiente: ")
    return opcion

def main():
    is_running = True
    sesiones = {}

    while is_running:
        opcion = menu_principal()

        if opcion == "1":
            print("\n*** Registro de nuevo usuario ***")
            registrar_usuario()
        elif opcion == "2":
            print("\n*** Iniciar sesión ***")
            usuario = login_usuario()
            if usuario:
                sesiones[usuario] = True  # Marcar la sesión como abierta
                proceso_compra(usuario, sesiones)  # Pasar 'sesiones' aquí
        elif opcion == "3":
            print("\n*** Mostrar usuarios ***")
            mostrar_usuarios()
        elif opcion == "4":
            proceso_compra(None, sesiones)  # Pasar 'sesiones' aquí también
        elif opcion == "5":
            print("\nSaliendo del programa...")
            is_running = False
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
