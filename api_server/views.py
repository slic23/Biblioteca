from django.shortcuts import render

from catalog.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class  libros(APIView):
    def get(self,request):
        libros = Book.objects.all()
        serial = listarLibros(libros,many=True)
        return Response(serial.data)


# Create your views here.


