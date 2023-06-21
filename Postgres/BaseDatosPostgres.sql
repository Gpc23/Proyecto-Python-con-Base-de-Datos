-- GONZALO PEÑA CALERO 1ºASIR        PROYECTO DE PYTHON CON BASE DE DATOS EN POSTGRES

-- Crear tabla Ganaderia
CREATE TABLE Ganaderia
(
Codigo INTEGER,
Nombre VARCHAR,
Localidad VARCHAR,
Procedencia VARCHAR,
Antiguedad INTEGER,
CONSTRAINT PK_Codigo PRIMARY KEY (Codigo)
);


# Crear tabla Torero
CREATE TABLE Torero
(
DNI INTEGER,
Plaza_Nombre VARCHAR,
Nombre VARCHAR,
Apodo VARCHAR,
CONSTRAINT PK_Torero_DNI PRIMARY KEY (DNI)
);
    

-- Crear tabla Toro
CREATE TABLE Toro
(
Nombre VARCHAR(10),
Ganaderia_Codigo INTEGER,
Torero_DNI INTEGER,
Color VARCHAR,
CONSTRAINT PK_Nom PRIMARY KEY (Nombre),
CONSTRAINT FK_Ganaderia_Codigo FOREIGN KEY (Ganaderia_Codigo) REFERENCES Ganaderia (Codigo),
CONSTRAINT FK_Torero_DNI FOREIGN KEY (Torero_DNI) REFERENCES Torero (DNI)
);
    



INSERT INTO Toro values ('Toro1', '1', '49137848', TO_DATE('2001', 'yyyy'), 'negro', 'Ale');
INSERT INTO Toro values ('Toro2', '2', '49137846', TO_DATE('2002', 'yyyy'), 'gris', 'Mar');
INSERT INTO Toro values ('Toro3', '3', '49137845', TO_DATE('2003', 'yyyy'),'negro', 'Jose');

INSERT INTO Ganaderia values ('1', 'Ganaderia1', 'Leon', 'SORIA', '2003');
INSERT INTO Ganaderia values ('2', 'Ganaderia2', 'Zamora', 'SORIA', '2003');
INSERT INTO Ganaderia values ('3', 'Ganaderia3', 'Toledo', 'SORIA', '2003');

INSERT INTO Torero values ('49137848', 'Antonio', 'Pedro', 'ANTONI1');
INSERT INTO Torero values ('49137846', 'Rodrigo', 'Juan', 'RODRIO2');
INSERT INTO Torero values ('49137845', 'Luis', 'Carlos', 'LOLOLO3');