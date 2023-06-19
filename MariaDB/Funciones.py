# GONZALO PEÑA CALERO 1ºASIR        PROYECTO DE PYTHON CON BASE DE DATOS EN MARIADB

import sys
import MySQLdb
from tabulate import tabulate

def Conectar(host,usuario,password,database):
    try:
        db = MySQLdb.connect(host,usuario,password,database)
        return db
    except MySQLdb.Error as e:
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
    query = "SELECT Codigo,Nombre,Antiguedad FROM Ganaderia WHERE Antiguedad >= %s AND Antiguedad <= %s"

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

    query = "SELECT Nombre FROM Torero WHERE Apodo = %s"
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
    sql = "INSERT INTO Torero (DNI, Nombre, Apodo) VALUES ( %s, %s, %s)"
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
    sql = "DELETE FROM Ganaderia WHERE Codigo IN (SELECT Ganaderia_Codigo FROM Toro WHERE Nombre = %s)"
    cursor = db.cursor()
        
    try:
        cursor.execute(sql, (nombre))
        if cursor.rowcount == 0:
            print("No se encontraron registros relacionados en la tabla Ganaderia.")
        else:
            sql = "DELETE FROM Toro WHERE Nombre = %s"
            cursor.execute(sql, (nombre))
            db.commit()
            print("")
            print(f"Se borró las ganaderias y el toro con el nombre'{nombre}'.")
            print("")
    except:
        print("")
        print("Error al borrar el toro.")
        print("")
        db.rollback()
    


def Aumentar_antiguedad(db, porcentaje, nombre):
    sql = f"UPDATE Ganaderia SET Antiguedad = Antiguedad * '{1 + int(porcentaje)/100}' WHERE Codigo IN (SELECT Ganaderia_Codigo FROM Toro WHERE Nombre = '{nombre}')"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
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
            
    except:
        print("Error al cambiar")
        db.rollback()