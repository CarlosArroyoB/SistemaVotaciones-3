IF NOT EXISTS (SELECT 1 FROM sys.objects WHERE type = 'P' AND name = 'insertar_voto')
BEGIN
    EXEC('
        CREATE PROCEDURE insertar_voto  
            @votante_id NVARCHAR(20),  
            @candidato_id INT 
        AS  
        BEGIN  
            SET NOCOUNT ON;  

            -- Verificar si el votante existe
            IF NOT EXISTS (SELECT 1 FROM Votante WHERE numero_documento = @votante_id)  
            BEGIN  
                RAISERROR(''El votante con documento %s no existe.'', 16, 1, @votante_id);  
                RETURN;  
            END  

            -- Verificar si el candidato existe
            IF NOT EXISTS (SELECT 1 FROM Candidato WHERE id = @candidato_id)  
            BEGIN  
                RAISERROR(''El candidato con candidato_id %s no existe.'', 16, 1, @candidato_id);  
                RETURN;  
            END  

            -- Verificar si el votante ya ha votado
            IF EXISTS (SELECT 1 FROM Voto WHERE votante_id = @votante_id)  
            BEGIN  
                RAISERROR(''El votante con documento %s ya ha votado.'', 16, 1, @votante_id);  
                RETURN;  
            END  

            -- Insertar el voto
            INSERT INTO Voto (votante_id, candidato_id, fecha_voto)  
            VALUES (@votante_id, @candidato_id, GETDATE());  
        END
    ');
END;
