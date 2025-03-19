IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Votante')
BEGIN
    CREATE TABLE Votante (
        id INT IDENTITY(1,1) PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        apellidos VARCHAR(100) NOT NULL,
        tipo_documento VARCHAR(20) NOT NULL,
        numero_documento VARCHAR(20) UNIQUE NOT NULL,
        genero CHAR(1) CHECK (genero IN ('M', 'F')),
        localidad VARCHAR(10) NOT NULL CHECK (localidad IN ('A', 'B', 'C', 'D', 'E'))  
    );
END;

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Candidato')
BEGIN
    CREATE TABLE Candidato (
        id INT IDENTITY(1,1) PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        apellidos VARCHAR(100) NOT NULL,
        partido VARCHAR(100) NOT NULL,
        localidad VARCHAR(10) NOT NULL CHECK (localidad IN ('A', 'B', 'C', 'D', 'E'))  
    );
END;

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Voto')
BEGIN
    CREATE TABLE Voto (
        id INT IDENTITY(1,1) PRIMARY KEY,
        votante_id INT NOT NULL,
        candidato_id INT NOT NULL,
        fecha_voto DATETIME DEFAULT GETDATE(),
        FOREIGN KEY (votante_id) REFERENCES Votante(id),
        FOREIGN KEY (candidato_id) REFERENCES Candidato(id)
    );
END;
