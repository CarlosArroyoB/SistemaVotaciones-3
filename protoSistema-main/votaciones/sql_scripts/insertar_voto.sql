IF NOT EXISTS (SELECT 1 FROM sys.objects WHERE type = 'P' AND name = 'insertar_voto')
BEGIN
    EXEC('
        CREATE PROCEDURE insertar_voto  
            @numero_documento NVARCHAR(20),  
            @nombre_candidato NVARCHAR(100)  
        AS  
        BEGIN  
            SET NOCOUNT ON;  

            -- Verificar si el votante existe
            IF NOT EXISTS (SELECT 1 FROM Votante WHERE numero_documento = @numero_documento)  
            BEGIN  
                RAISERROR(''El votante con documento %s no existe.'', 16, 1, @numero_documento);  
                RETURN;  
            END  

            -- Verificar si el candidato existe
            IF NOT EXISTS (SELECT 1 FROM Candidato WHERE nombre = @nombre_candidato)  
            BEGIN  
                RAISERROR(''El candidato con nombre %s no existe.'', 16, 1, @nombre_candidato);  
                RETURN;  
            END  

            -- Verificar si el votante ya ha votado
            IF EXISTS (SELECT 1 FROM Voto WHERE numero_documento = @numero_documento)  
            BEGIN  
                RAISERROR(''El votante con documento %s ya ha votado.'', 16, 1, @numero_documento);  
                RETURN;  
            END  

            -- Insertar el voto
            INSERT INTO Voto (numero_documento, nombre_candidato, fecha_hora)  
            VALUES (@numero_documento, @nombre_candidato, GETDATE());  
        END
    ');
END;
