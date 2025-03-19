from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import VotanteSerializer, CandidatoSerializer,VotoSerializer

@api_view(['POST'])
def registrar_votante(request):
    serializer = VotanteSerializer(data=request.data)

    if serializer.is_valid():
        datos = serializer.validated_data

        with connection.cursor() as cursor:
            try:
                cursor.execute("EXEC dbo.insertar_votante %s, %s, %s, %s, %s, %s", 
                    [
                        datos["nombre"], datos["apellidos"], datos["tipo_documento"],
                        datos["numero_documento"], datos["genero"], datos["localidad"]
                    ]
                )
                return Response({"message": "Votante registrado con éxito"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def registrar_candidato(request):
    serializer = CandidatoSerializer(data=request.data)

    if serializer.is_valid():
        datos = serializer.validated_data
        with connection.cursor() as cursor:
            try:
                cursor.execute("EXEC dbo.insertar_candidato  %s, %s, %s", 
                    [
                        datos["nombre"], datos["partido"], datos["localidad"]
                    ]
                )
                return Response({"message": "Candidato registrado con éxito"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def registrar_voto(request):
    serializer = VotoSerializer(data=request.data)

    if serializer.is_valid():
        datos = serializer.validated_data
        numero_documento = datos["votante_id"]  # Número de documento del votante
        candidato_id = datos["candidato_id"]  # ID del candidato (entero)

        with connection.cursor() as cursor:
            try:
                # Llamar al procedimiento almacenado con los datos recibidos
                cursor.execute("EXEC insertar_voto %s, %s", [numero_documento, candidato_id])
                return Response({"message": "Voto registrado con éxito"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)