

from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import VotanteSerializer

@api_view(['POST'])
def registrar_votante(request):
    serializer = VotanteSerializer(data=request.data)

    if serializer.is_valid():
        datos = serializer.validated_data

        with connection.cursor() as cursor:
            try:
                cursor.execute("EXEC sistVotaciones.dbo.insertar_votante %s, %s, %s, %s, %s, %s", 
                    [
                        datos["nombre"], datos["apellidos"], datos["tipo_documento"],
                        datos["numero_documento"], datos["genero"], datos["localidad"]
                    ]
                )
                return Response({"message": "Votante registrado con éxito"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

