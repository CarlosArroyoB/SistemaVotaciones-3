from rest_framework import serializers

class VotanteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=100)
    apellidos = serializers.CharField(max_length=100)
    tipo_documento = serializers.CharField(max_length=20)
    numero_documento = serializers.CharField(max_length=20)
    genero = serializers.CharField(max_length=1)
    localidad = serializers.CharField(max_length=10)
