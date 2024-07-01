import os
informe = []
marca = ['kia','ford','nissan']
titulo = """ REGISTROS DE VEHICULOS
-----------------------------------------------------------------------------------
Marca Año Kilo Costo Impuesto Costo total
-----------------------------------------------------------------------------------
"""
def registrar():
    while True:
        try:
            mar = input("Ingrese marca del vehiculo: ").strip().lower()
            año = int(input("Ingrese año de fabricacion: "))
            kilo = int(input("Ingrese kilometraje del vehiculo: "))
            costo = int(input("Ingrese costo de reparacion estimado: "))
            imp = round(costo * 0.08)
            total = round(costo + imp)
            if mar and marca and año>1920 and kilo>0 and costo>0:
                informe.append([mar,año,kilo,costo,imp,total])
                input("Ingresado correctamente")
                os.system("cls")
                break
            else:
                input("Error de ingreso")
        except Exception as e:
            input(f"Excepsion de ingreso {str(e)}: ")
def listatodo():
    salida = titulo
    for t in informe:
        salida += f"{t[0]:10s}"
        salida += f"{t[1]:9d}"
        salida += f"{t[2]:12d}"
        salida += f"{t[3]:14d}"
        salida += f"{t[4]:14d}"
        salida += f"{t[5]:19d}"
        salida += "\n"
    return salida
def listamarca(marca):
    salida = titulo
    for t in informe:
        if marca == t[0]:
            salida += f"{t[0]:10s}"
            salida += f"{t[1]:9d}"
            salida += f"{t[2]:12d}"
            salida += f"{t[3]:14d}"
            salida += f"{t[4]:14d}"
            salida += f"{t[5]:19d}"
            salida += "\n"
    return salida
def imprimir():
    x = input(f"informe a imprimir [todos/{marca}]: ").strip().lower()
    if x == "todos":
        with open("informe.txt", "w") as archivo:
            archivo.write(listatodo())
    elif x in marca:
        with open("informe.txt", "w") as archivo:
            archivo.write(listamarca(x))
    else:
        input("Error de ingreso: ")
while True:
    try:
        menu = int(input("""
         1. Registrar Vehiculo
         2. Listar todos los vehiculos registrados:
         3. Imprimir orden de Reperacion
         4. Salir del programa
         Digite la opcion deseada: """))
        if menu == 1:
            registrar()
        elif menu == 2:
            print(listatodo())
        elif menu == 3:
            imprimir()
        elif menu == 4:
            break
        else:
            input("Error de ingreso")
    except Exception as e:
        input(f"Excepcion de menu {str(e)}: ")