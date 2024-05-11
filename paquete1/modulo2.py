# Función para registrar un usuario
def registrar_usuario(base_datos):
    retry = True

    while retry:
        usuario = input("Ingrese nombre de usuario: ")
        if usuario in base_datos:
            print("El nombre de usuario ya existe. Por favor, elija otro.")
        elif len(usuario) >15: 
            print("El usuario debe contener menos de 15 caracteres")
        else:
            contraseña = input("Ingrese contraseña (debe tener entre 6 y 15 caracteres y contener al menos un número, una letra mayúscula y un caracter especial): ")
            if len(contraseña) < 6 or len(contraseña) > 15:
                print("La contraseña es demasiado corta. Debe tener al menos 6 caracteres.")            
            elif not any(caracter.isdigit() for caracter in contraseña):
                print("La contraseña debe contener al menos un número.")
            elif not any(caracter.isupper() for caracter in contraseña):
                print("La contraseña debe contener al menos una letra mayúscula.")    
            elif not any(caracter in "!@#$%^&*()-_+=[]{};:,.<>?/" for caracter in contraseña):
                print("La contraseña debe contener al menos un caracter especial.")
            else:
                # Validación de la contraseña
                contraseña_confirmacion = input("Confirme la contraseña: ")
                if contraseña != contraseña_confirmacion:
                    print("Las contraseñas no coinciden. Por favor, inténtelo de nuevo.")
                    continue
                else:
                    # Almacenar el usuario y la contraseña
                    base_datos[usuario] = contraseña
                    retry = False
                    print("Usuario registrado exitosamente.")

# Función para mostrar la información de usuarios registrados
def mostrar_usuarios(base_datos):
    if base_datos:
        print("Usuarios registrados:")
        for usuario, contraseña in base_datos.items():
            print(f"Usuario: {usuario}, Contraseña: {contraseña}")
    else:
        print("No hay usuarios registrados.")

# Función para el login de usuarios
def login_usuario(base_datos):
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    if usuario in base_datos and base_datos[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

# Función principal
def main():
    base_datos = {}
    is_running = True

    while is_running:
        is_wrong_answer = True
        while is_wrong_answer:
            print("\nBienvenido al sistema de gestión de usuarios:")
            print("1. Registrar un nuevo usuario")
            print("2. Mostrar usuarios registrados")
            print("3. Iniciar sesión")
            print("4. Salir")
            opcion = input("Seleccione una opción ingresando el número correspondiente: ")
            
            # Validar entrada del usuario
            try:
                opcion = int(opcion) 
                if opcion < 1 or opcion > 4:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
                else:
                    is_wrong_answer = False
            except ValueError:
                print("Por favor, ingrese un número válido.")
                           
                  
        if opcion == 1:
            print("\n*** Registro de nuevo usuario ***")
            registrar_usuario(base_datos)
        elif opcion == 2:
            print("\n*** Usuarios registrados ***")
            mostrar_usuarios(base_datos)
        elif opcion == 3:
            print("\n*** Iniciar sesión ***")
            login_usuario(base_datos)
        elif opcion == 4:
            print("\nSaliendo del programa...")
            is_running = False
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# Llamada a la función principal
main()