# GONZALO PEÑA CALERO 1ºASIR        PROYECTO DE PYTHON CON BASE DE DATOS EN MARIADB

import mysql.connector

#Creamos primero la base de datos

#Create Database mariapy

# Establecer conexión con la base de datos
cnx = mysql.connector.connect(
    user='gonzalo',
    password='gonzalo',
    host='localhost',
    database='mariapy'
)

cursor = cnx.cursor()

# Crear tabla Toro
table_toro = (
    "Nombre              VARCHAR2(10),"
    "Ganaderia_Codigo    NUMBER,"
    "Torero_DNI          NUMBER,"
    "Ano_Nacimiento      DATE,"
    "Color               VARCHAR2(10),"
    "Piccador            VARCHAR2(10),"
    "CONSTRAINT PK_Nom PRIMARY KEY (Nombre),"
    "CONSTRAINT FK_Ganaderia_Codigo FOREIGN KEY (Ganaderia_Codigo) REFERENCES Ganaderia (Codigo),"
    "CONSTRAINT FK_Torero_DNI FOREIGN KEY (Torero_DNI) REFERENCES Torero (DNI)"
    )
    
cursor.execute(table_toro)


# Crear tabla Ganaderia
table_ganaderia = (
    "Codigo              NUMBER,"
    "Nombre              VARCHAR2(10),"
    "Localidad           VARCHAR2(10),"
    "Procedencia         VARCHAR2(10),"
    "Antiguedad          NUMBER,"
    "CONSTRAINT PK_Codigo PRIMARY KEY (Codigo)"
    )
    
cursor.execute(table_ganaderia)


# Crear tabla Torero
table_torero = (
    "DNI                 NUMBER,"
    "Nombre              VARCHAR2(10),"
    "Apodo               VARCHAR2(10),"
    "CONSTRAINT PK_Torero_DNI PRIMARY KEY (DNI)"
    )
    
cursor.execute(table_torero)




query1 =("INSERT INTO Toro values ('Toro1', '1', '49137848',TO_DATE('2001', 'yyyy'), 'negro', 'Ale')")
query2 =("INSERT INTO Toro values ('Toro2', '2', '49137846',TO_DATE('2002', 'yyyy'), 'gris', 'Mar')")
query3 =("INSERT INTO Toro values ('Toro3', '3', '49137845',TO_DATE('2003', 'yyyy'),'negro', 'Jose')")


query4 =("INSERT INTO Ganaderia values ('1', 'Ganaderia1', 'Leon', 'SORIA', '2003')")
query5 =("INSERT INTO Ganaderia values ('2', 'Ganaderia2', 'Zamora', 'SORIA', '2004')")
query6 =("INSERT INTO Ganaderia values ('3', 'Ganaderia3', 'Toledo', 'SORIA', '2005')")

query7 =("INSERT INTO Torero values ('49137848', 'Antonio', 'Pedro', 'Antoni1')")
query8 =("INSERT INTO Torero values ('49137846', 'Rodrigo', 'Juan', 'Rodrio2')")
query9 =("INSERT INTO Torero values ('49137845', 'Luis', 'Carlos', 'Lololo3')")

cursor.execute(query1)
cursor.execute(query2)
cursor.execute(query3)
cursor.execute(query4)
cursor.execute(query5)
cursor.execute(query6)
cursor.execute(query7)
cursor.execute(query8)
cursor.execute(query9)

cnx.commit()

# Cerrar el cursor y la conexión
cursor.close()
cnx.close()