from rest_framework import serializers
from core.models import Libro
class LibroSerializer(serializers.ModelSerializer):
    class meta:
        model = Libro
        fields = ['id','titolo','autore','genere']

