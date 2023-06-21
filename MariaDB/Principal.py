# GONZALO PEÑA CALERO 1ºASIR        PROYECTO DE PYTHON CON BASE DE DATOS EN MARIADB

import mysql.connector 
from Funciones import *

try:
    db = mysql.connector.connect(
        user='gonzalo',
        password='gonzalo',
        host='localhost',
        database='mariapy'
)

except mysql.connector.Error as err:
    print(f"Error de conexión: {err}")
    exit(1)

# Crear cursor
cursor = db.cursor()

salir = False

while not salir:
    print("1. Listar Ganaderias")
    print("2. Buscar la ganaderia por intervalos de antiguedad")
    print("3. Buscar el nombre del torero por el apodo")
    print("4. Insertar nuevo Torero")
    print("5. Borra las ganaderias por el nombre identificativo del toro")
    print("6. Aumentar la antiguedad de ganaderia de un toro con su nombre")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")


    if opcion == "1":
        ganaderia = Listar_ganaderia(db)
        if ganaderia:
            for a in ganaderia:
                print(a)
    


    elif opcion=="2":
        
        print("Introduce los Valores:")
        print("")
        valor_min=input("Minimo 2003: ")
        valor_max=input("Maximo 2005: " )
        print("")
    
        Buscar_ganaderia(db,valor_min, valor_max)



    elif opcion=="3":
        apodo = input("Ingrese el apodo: ")
        
        torero =Buscar_torero(db,apodo)

        if torero is not None:
                print("")
                print("-----------------------------------------------------------")
                print(f"El torero con apodo {apodo} es {torero}.")
                print("-----------------------------------------------------------")
                print("")
        else:
                print("")
                print("------------------------------------------------------")
                print(" No se encontró ningun torero con ese apodo.")
                print("------------------------------------------------------")
                print("")



    elif opcion == "4":
        nuevo = {}
        print("")
        try:
            nuevo["DNI"] = input("DNI (8 digitos): ")
            nuevo["Nombre"] = input("Nombre: ")
            nuevo["Apodo"] = input("Apodo: ")
        except:
            print("Error al ingresar datos. Por favor, inténtelo de nuevo.")
            continue
        print("")
        print("")
        Inserta_Torero(db, nuevo)
        print("")
        print("")



    elif opcion == "5":
        nombre = input("Ingrese el nombre del toro: ")
        Borrar(db, nombre)



    elif opcion == "6":
        
        porcentaje= input("Porcentajes que deseas aumentar (Recuerda que son años lo que estas aumentando): ")
        nombre=input("Toro que deseas aumentar sus ganaderias: ")

        Aumentar_antiguedad(db, porcentaje, nombre)
    


    elif opcion == "7":
        salir = True
        print("")
        print("¡¡¡HASTA LA PROXIMA!!!")