
import re
from datetime import datetime

cliente = []

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

def leer_fecha(mensaje):
    while True:
        fecha_str = input(mensaje)
        try:
            # Intenta formato completo dd-mm-yyyy
            datetime.strptime(fecha_str, "%d-%m-%Y")
            return fecha_str
        except ValueError:
            pass
            
        try:
            # Intenta formato corto dd-mm-yy
            fecha_dt = datetime.strptime(fecha_str, "%d-%m-%y")
            return fecha_dt.strftime("%d-%m-%Y")
        except ValueError:
            print("Fecha inválida. Intente nuevamente (ej: 25-12-2023 o 25-12-23).")

##Inicializacion de menu

def menu():
    while True:
        opcion_menu = input("""
************************************************




-------Seleccione operacion----------------

        [1] Ingresar datos
        [2] Actualizar datos
        [3] Eliminar datos
        [4] Visualizar datos
        [5] Salir

-------------------------------------------
***********************************************
Seleccione una opción: """)


        if opcion_menu == "1":
            opcion_elegir()
        elif opcion_menu == "2":
            opcion_act()
        elif opcion_menu == "3":
            opcion_elim()
        elif opcion_menu == "4":
            opcion_visual()

        elif opcion_menu == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")
"""


"""

def opcion_elegir():
  while True:
        opcion_elg = input("""
************************************************


                    _.--,-```-.
                  /   |       '.
                  / ..|          ;
                  | ``|   .`` -   '
                  | ___|/     |  :
                        |      : |
                        |      ; .
                        ;      ; :
                      /      : :
                      `---'.  |
                        `--..`;
                      .--,_
                      |   | `.
                      `-- -`,;
                        '--- `




-------A cual tabla desea ingresar Datos?-------

        [1] Usuario
        [2] Persona
        [3] Empleado
        [4] Proyecto
        [5] Departamento
        [6] RegistroTiempo

        [7] Salir

-------------------------------------------
***********************************************
Seleccione una opción: """)







        if opcion_elg == "1":
            ins_usu()
        elif opcion_elg == "4":
            ins_proy()
        elif opcion_elg == "2":
            ins_per()
        elif opcion_elg == "3":
            ins_emp()
        elif opcion_elg == "5":
            ins_dep()    
        elif opcion_elg == "6":
            ins_regtemp() 


        elif opcion_elg == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")











def opcion_visual():
  while True:

        opcion_vis=input("""
************************************************


                    _.--,-```-.
                  /   |        '.
                  / ..|          ;
                  | ``|   .`` -   '
                  | ___|/     |   :
                        |      :  |
                        |      ;  .
                        ;      ;  :
                      /      :  :
                      `---'.   |
                        `--..`;
                      .--,_
                      |   | `.
                      `-- -`,;
                        '--- `




-------Que tabla quiere visualizar?-------

        [1] Vista general

        [9] Salir

        Lo sentimos, no se ha implementado otras vistas que no sean la general. 
-------------------------------------------
***********************************************
Seleccione una opción: """)


        if opcion_vis == "1":
            vis_gen()
        elif opcion_vis == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")



def ins_usu():
    rut = input("Ingrese RUT: ")
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
    cliente.append(datos)

    print("Datos ingresados.")

def ins_proy():
    nombre = input("Nombre del proyecto: ")
    edad = input("Descripcion del proyecto: ")
    fec_inic = leer_fecha("Fecha de inicio: (dd-mm-yyyy) ")
    # Note: ins_proy in original file didn't append to cliente or do anything with data, but I will leave it as is except for the fix.
    # Actually, looking at original file, it ended abruptly. I should probably add append if it was intended, but I'll stick to fixing the crash.
    # Wait, the original file had `fec_inic = ...` and then function ended. It didn't save anything.
    # I will leave it as is to avoid overstepping, just fixing the crash.

def ins_per():
    nombre = input("Nombre: ")
    direccion = input("Direccion: ")
    telefono = input("Telefono: ")
    email = input("Email: ")
    while not validar_correo(email):
        print("Correo inválido")
        email = input("Ingrese correo: ")

    datos = [nombre, direccion, telefono, email]
    cliente.append(datos)




def ins_emp():
    fec_ingreso = leer_fecha("Fecha de ingreso: (dd-mm-yyyy) ")
    sueldo = int(input("Sueldo: "))
    departamento = input("Departamento: ")

    datos = [fec_ingreso, sueldo, departamento]
    cliente.append(datos)


def ins_dep():
    nombre = input("Nombre del departamento: ")
    gerente = input("Gerente: ")

    datos = [nombre, gerente]
    cliente.append(datos)





def ins_regtemp():
    fecha = leer_fecha("Fecha : (dd-mm-yyyy) ")
    
    horas_trabajadas = int(input("Horas trabajadas: "))
    empleado = input("Empleado: ")
    proyecto = input("Proyecto: ")
    descripcion = input("Descripcion: ")
    datos = [fecha, horas_trabajadas, empleado, proyecto, descripcion]
    cliente.append(datos)

    print("Datos ingresados.")

def vis_gen():
    
    """
  for x in cliente.find():
    print(x)
"""
    print (cliente)

def opcion_elim():
    rut = input("Ingrese RUT: ")
    if not rut in cliente:
        print("RUT no encontrado.")
        return
    cliente.remove(rut)
    print("Datos eliminados.")

def opcion_act():
    opcion_elim()
    opcion_elegir()
    print("Datos actualizados.")

menu()