import os
import re
import json

ruta_archivo = os.path.join(os.getcwd(), "usuarios.json")

def leerData():
    if not os.path.exists(ruta_archivo):
        return {}

    try:
        with open(ruta_archivo, "r", encoding='utf-8') as f:
            base_datos = json.load(f)
        return base_datos
    except json.decoder.JSONDecodeError:
        print(f"La lista está vacía. ¡Debes guardar información primero!")
        return {}
    except FileNotFoundError:
        print("La lista no se encontró o está vacía aún")
        return {}

def validar_contrasena(contrasena):
    if len(contrasena) < 6 or len(contrasena) > 15:
        return False
    if not re.search(r"\d", contrasena):
        return False
    if not re.search(r"[A-Z]", contrasena):
        return False
    if not re.search(r"[!@#$%^&*()-_+=\[\]{};:,.<>?/]", contrasena):
        return False
    return True

def guardar_data(base_datos):
    try:
        with open(ruta_archivo, "w", encoding='utf-8') as f:
            json.dump(base_datos, f, indent=2)
            print("Datos guardados exitosamente.")
    except Exception as e:
        print("Error al guardar los datos:", e)

def registrar_usuario():
    base_datos = leerData()
    retry = True

    while retry:
        nombre = input("Ingrese su nombre: ")
        print("———————————————————————————————————————————————————————")
        while True:
            edad = input("Ingrese su edad: ")
            if not edad.isdigit():
                print("Edad inválida. Por favor, ingrese un número entero.")
            else:
                edad = int(edad)
                break
        email = input("Ingrese su email: ")
        print("———————————————————————————————————————————————————————")
        usuario = input("Ingrese nombre de usuario: ")
        if usuario in base_datos:
            print("El nombre de usuario ya existe. Por favor, elija otro.")
        elif len(usuario) > 15: 
            print("El usuario debe contener menos de 15 caracteres")
        else:
            print("———————————————————————————————————————————————————————")
            if usuario in base_datos:
                intereses = base_datos[usuario]["intereses"]
                print(f"Tus intereses registrados son: {intereses}")
                confirmacion = input("¿Desea mantener estos intereses? (s/n): ")
                if confirmacion.lower() == "n":
                    intereses = input("Ingrese sus intereses: ")
            else:
                intereses = input("Ingrese sus intereses: ")
            print("———————————————————————————————————————————————————————")
            contrasena = input("Ingrese contraseña (debe tener entre 6 y 15 caracteres y contener al menos un número, una letra mayúscula y un caracter especial): ")
            if not validar_contrasena(contrasena):
                print("La contraseña no cumple con los requisitos de seguridad.")
                continue
            else:
                contrasena_confirmacion = input("Confirme la contraseña: ")
                if contrasena != contrasena_confirmacion:
                    print("Las contraseñas no coinciden. Por favor, inténtelo de nuevo.")
                    continue
                else:
                    base_datos[usuario] = {
                        "nombre": nombre,
                        "edad": edad,
                        "email": email,
                        "intereses": intereses,
                        "contraseña": contrasena,
                        "productos": []
                    }
                    guardar_data(base_datos)
                    retry = False
                    print("Usuario registrado exitosamente.")
                    return usuario

def mostrar_usuarios():
    base_datos = leerData()
    if base_datos:
        print("Usuarios registrados:")
        for usuario, datos in base_datos.items():
            print(f"Usuario: {usuario}, Datos: {datos}")
    else:
        print("No hay usuarios registrados.")

sesiones = {}

def login_usuario():
    base_datos = leerData()
    usuario = input("Ingrese nombre de usuario: ")
    contrasena = input("Ingrese contraseña: ")
    if usuario in base_datos and base_datos[usuario]["contraseña"] == contrasena:
        sesiones[usuario] = base_datos[usuario]
        print("Inicio de sesión exitoso.")
        return usuario
    else:
        print("Nombre de usuario o contraseña incorrectos.")
