IF NOT EXISTS (SELECT 1 FROM sys.objects WHERE type = 'P' AND name = 'insertar_votante')
BEGIN
    EXEC('
        CREATE PROCEDURE insertar_votante  
            @nombre NVARCHAR(100),  
            @apellidos NVARCHAR(100),  
            @tipo_documento NVARCHAR(20),  
            @numero_documento NVARCHAR(20),  
            @genero CHAR(1),  
            @localidad NVARCHAR(10)  
        AS  
        BEGIN  
            SET NOCOUNT ON;  

            -- Verificar si el votante ya existe
            IF EXISTS (SELECT 1 FROM Votante WHERE numero_documento = @numero_documento)  
            BEGIN  
                DECLARE @mensaje NVARCHAR(255);  
                SELECT @mensaje = ''El votante con '' + tipo_documento + '' de número '' + numero_documento + '' ya está registrado.''  
                FROM Votante WHERE numero_documento = @numero_documento;  
                
                RAISERROR(@mensaje, 16, 1);  
                RETURN;  
            END  

            -- Insertar nuevo votante
            INSERT INTO Votante (nombre, apellidos, tipo_documento, numero_documento, genero, localidad)  
            VALUES (@nombre, @apellidos, @tipo_documento, @numero_documento, @genero, @localidad);  
        END
    ');
END;
