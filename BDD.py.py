import os
import re

def rut_rep(rut):
    try:
        with open("bdd.txt", "r") as archivo:
            for linea in archivo:
                if rut in linea:
                    print("RUT ya ingresado...")
                    return True
        return False
    except FileNotFoundError:
        print("El archivo no existe.")
        return False

def validar_rut(rut):
    rut = rut.upper().replace("-", "").replace(".", "").replace(",", "")
    aux = rut[:-1]
    dv = rut[-1]

    revertido = map(int, reversed(str(aux)))
    factores = [2, 3, 4, 5, 6, 7] * 2
    s = sum(d * f for d, f in zip(revertido, factores))
    res = 11 - (s % 11)
    if res == 10:
        res = "K"
    elif res == 11:
        res = "0"
    return str(res) == dv

def validar_correo(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, correo) is not None

def ingresar_datos():
    rut = input("Ingrese RUT: ")
    while rut_rep(rut):
        rut = input("Ingrese un RUT que no exista: ")
    while not validar_rut(rut):
        print("RUT inválido")
        rut = input("Ingrese RUT: ")

    nombre = input("Ingrese nombre: ")
    edad = input("Ingrese edad: ")
    correo = input("Ingrese correo: ")
    while not validar_correo(correo):
        print("Correo inválido")
        correo = input("Ingrese correo: ")

    datos = [rut, nombre, edad, correo]
    with open("bdd.txt", "a") as archivo:
        linea = ", ".join(datos) + "\n"
        archivo.write(linea)

    print("Datos ingresados.")

def leer_datos():
    if not os.path.exists("bdd.txt"):
        print("El archivo no existe.")
        return

    with open("bdd.txt", "r") as archivo:
        lineas = archivo.readlines()
        if not lineas:
            print("No hay datos registrados.")
            return

        print("\nDatos:\n")
        for i, linea in enumerate(lineas, start=1):
            datos = linea.strip().split(', ')
            rut, nombre, edad, correo = datos
            print(f"{i}) RUT: {rut}, Nombre: {nombre}, Edad: {edad}, Correo: {correo}")
        print("\n------------------------------------------------------------")

def eliminar_datos():
    rut = input("Ingrese el RUT del usuario que desea eliminar: ")
    if not os.path.exists("bdd.txt"):
        print("No hay datos para eliminar.")
        return

    with open("bdd.txt", "r") as archivo:
        lineas = archivo.readlines()

    nuevas_lineas = []
    eliminado = False

    for linea in lineas:
        if rut in linea:
            datos = linea.strip().split(', ')
            nombre = datos[1]
            print(f"Datos encontrados: {linea.strip()}")
            conf = input("¿Es este el RUT que desea eliminar? (S/N): ").upper()
            if conf == "S":
                try:
                    os.remove(f"{nombre}.txt")
                except FileNotFoundError:
                    print("Archivo del usuario no encontrado.")
                eliminado = True
                continue
        nuevas_lineas.append(linea)

    with open("bdd.txt", "w") as archivo:
        archivo.writelines(nuevas_lineas)

    if eliminado:
        print("Usuario eliminado.")
    else:
        print("Usuario no eliminado.")

def actualizar_datos():
    eliminar_datos()
    ingresar_datos()


def menu():
    while True:
        opcion = input("""
***************************************
        [1] Ingresar datos
        [2] Actualizar datos
        [3] Eliminar datos
        [4] Visualizar datos         
        [5] Salir
***************************************
Seleccione una opción: """)

        if opcion == "1":
            ingresar_datos()
        elif opcion == "2":
            actualizar_datos()
        elif opcion == "3":
            eliminar_datos()
        elif opcion == "4":
            leer_datos()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()