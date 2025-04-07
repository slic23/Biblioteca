from rest_framework import serializers
from catalog.models import *

class listarLibros(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        
        