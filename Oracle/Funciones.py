# GONZALO PEÑA CALERO 1ºASIR        PROYECTO DE PYTHON CON BASE DE DATOS EN ORACLE

import sys
import cx_Oracle

def Conectar(user,password,dsn):
    try:
        db = cx_Oracle.connect(user,password,dsn)
        return db
    except cx_Oracle.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)

def Desconectar_BD(db):
    db.close()



def Listar_ganaderia(db):
    
    cursor = db.cursor()
    query = "SELECT * FROM Ganaderia"
    cursor.execute(query)
    Ganaderia = cursor.fetchall()
    cursor.close()
    return Ganaderia



def Buscar_ganaderia(db,min_val, max_val):
    
    cursor = db.cursor()

    print("Búsqueda de ganaderias:")
    print("")
    query = "SELECT Codigo,Nombre,Antiguedad FROM Ganaderia WHERE Antiguedad >= :min_val AND Antiguedad <= :max_val"

    cursor.execute(query, min_val=min_val, max_val=max_val)

    resultados = cursor.fetchall()

    resultadoss= False

    for row in resultados:
        resultadoss = True
        print("Codigo\t\Nombre\t\Antiguedad")
        print("-----------------------------------------------------------")
        print(f"{row[0]}\t{row[1]}\t{row[2]}")
        print("")
        print("")
    
    if not resultadoss:
        print("No se encontraron resultados")
        print("")
        print("")
    cursor.close()



def Buscar_torero(db,apodo):
   
    cursor = db.cursor()

    query = "SELECT Nombre FROM Torero WHERE Apodo = :Apodo"
    cursor.execute(query,{'apodo': apodo})

    resultado = cursor.fetchone()

    cursor.close()

    if resultado is not None:
        return resultado[0]
    else:
        return None
    


def Inserta_Torero(db, nuevo):
    cursor = db.cursor()
    print("Insertar nuevos registros en Torero: ")
    print("")
    sql = "INSERT INTO Torero (DNI, Nombre, Apodo) VALUES ( :1, :2, :3)"
    values = (nuevo["DNI"], nuevo["Nombre"], nuevo["Apodo"])
    cursor.execute(sql, values)
    
    try:
        db.commit()
        print("")
        print("Insertado correctamente")
        print("")
    except:
        print("Error al insertar.")
        db.rollback()



def Borrar(db, nombre):
    try:
        cursor = db.cursor()
        sql = "DELETE FROM Ganaderia WHERE Codigo IN (SELECT Ganaderia_Codigo FROM Toro WHERE Nombre = :nombre)"
        cursor.execute(sql, {'nombre': nombre})
        
        if cursor.rowcount == 0:
            print("No se encontraron registros relacionados en la tabla Ganaderia.")
        else:
            sql = "DELETE FROM Toro WHERE Nombre = :nombre"
            cursor.execute(sql, {'nombre': nombre})
            db.commit()
            print("")
            print(f"Se borró las ganaderias y el toro con el nombre'{nombre}'.")
            print("")
    except:
        print("")
        print("Error al borrar el toro.")
        print("")
        db.rollback()
    


def Aumentar_antiguedad(db, porcentaje, Nombre):

    try:
        porcentaje = int(porcentaje)
    except ValueError:
        print("El porcentaje no es un número válido.")
        return
    
    cursor = db.cursor()
    try:
       
        sql = "UPDATE Ganaderia SET Antiguedad = Antiguedad * :factor WHERE Codigo IN (SELECT Ganaderia_Codigo FROM Toro WHERE Nombre = :nombre)"
        cursor.execute(sql, {'factor': 1 + porcentaje/100, 'nombre': Nombre})
        db.commit()
        
        if cursor.rowcount == 0:
            print("")
            print("-----------------------------------------------------------")
            print("No se encontró un toro con ese nombre")
            print("-----------------------------------------------------------")
            print("")
        else:
            print("")
            print("------------------------------------------------")
            print(f"Se han actualizado {cursor.rowcount} ganaderias.")
            print("------------------------------------------------")
            print("")
            
    except cx_Oracle.DatabaseError as e:

        print("Error al cambiar:", e)
        db.rollback()