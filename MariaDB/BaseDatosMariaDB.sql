-- GONZALO PEÑA CALERO 1ºASIR        PROYECTO DE PYTHON CON BASE DE DATOS EN MARIADB

-- Crear tabla Ganaderia
CREATE TABLE Ganaderia
(
Codigo INT,
Nombre VARCHAR(10),
Localidad VARCHAR(10),
Procedencia VARCHAR(10),
Antiguedad INT,
CONSTRAINT PK_Codigo PRIMARY KEY (Codigo)
);


-- Crear tabla Torero
CREATE TABLE Torero
(
DNI INT,
Plaza_Nombre VARCHAR(10),
Nombre VARCHAR(10),
Apodo VARCHAR(10),
CONSTRAINT PK_Torero_DNI PRIMARY KEY (DNI)
);
    

-- Crear tabla Toro
CREATE TABLE Toro
(
Nombre VARCHAR(10),
Ganaderia_Codigo INT,
Torero_DNI INT,
Ano_Nacimiento DATETIME,
Color VARCHAR(10),
Piccador VARCHAR(10),
CONSTRAINT PK_Nom PRIMARY KEY (Nombre),
CONSTRAINT FK_Ganaderia_Codigo FOREIGN KEY (Ganaderia_Codigo) REFERENCES Ganaderia (Codigo),
CONSTRAINT FK_Torero_DNI FOREIGN KEY (Torero_DNI) REFERENCES Torero (DNI)
);
    


INSERT INTO Toro values ('Toro1', '1', '49137848', STR_TO_DATE('2001', '%Y'), 'negro', 'Ale');
INSERT INTO Toro values ('Toro2', '2', '49137846', STR_TO_DATE('2002', '%Y'), 'gris', 'Mar');
INSERT INTO Toro values ('Toro3', '3', '49137845', STR_TO_DATE('2003', '%Y'), 'negro', 'Jose');


INSERT INTO Ganaderia values ('1', 'Ganaderia1', 'Leon', 'SORIA', '2003');
INSERT INTO Ganaderia values ('2', 'Ganaderia2', 'Zamora', 'SORIA', '2004');
INSERT INTO Ganaderia values ('3', 'Ganaderia3', 'Toledo', 'SORIA', '2005');

INSERT INTO Torero values ('49137848', 'Antonio', 'Pedro', 'Antoni1');
INSERT INTO Torero values ('49137846', 'Rodrigo', 'Juan', 'Rodrio2');
INSERT INTO Torero values ('49137845', 'Luis', 'Carlos', 'Lololo3');

