IF NOT EXISTS (SELECT 1 FROM sys.objects WHERE type = 'P' AND name = 'insertar_candidato')
BEGIN
    EXEC('
        CREATE PROCEDURE insertar_candidato  
            @nombre NVARCHAR(100),  
            @partido NVARCHAR(100), 
            @localidad NVARCHAR(10)  
        AS  
        BEGIN  
            SET NOCOUNT ON;  

            -- Verificar si el votante ya existe
            IF EXISTS (SELECT 1 FROM Votante WHERE nombre = @nombre)  
            BEGIN  
                DECLARE @mensaje NVARCHAR(255);  
                SELECT @mensaje = ''El candidato de nombre:  '' + nombre + '' Ya se encuentra registrado ''   
                FROM Votante WHERE nombre = @nombre;  
                
                RAISERROR(@mensaje, 16, 1);  
                RETURN;  
            END  

            -- Insertar nuevo votante
            INSERT INTO Candidato (nombre, partido, localidad)  
            VALUES (@nombre, @partido, @localidad);  
        END
    ');
END;
