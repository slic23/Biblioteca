from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def index(request):

    """
    funcion principal del sitio catalog

    """

    num_libros = Book.objects.all().count()
    numero_ejemplares = BookInstance.objects.all().count()
    ejemplares_disponibles = BookInstance.objects.filter(status__exact='a').count()
    numero_autores = Author.objects.all().count()
    numero_generos = Genre.objects.all().count()
    palabra_numeroVeces = Book.objects.filter(title__icontains= 'la').count()

    contexto = {
        'numero_libros':num_libros,
        'numero_ejemplares': numero_ejemplares,
        'ejemplares_disponibles': ejemplares_disponibles,
        'numero_autores':numero_autores,
        'numero_generos':numero_generos,
        'palabrasEncontradas':palabra_numeroVeces

    }


    return render(request,'index.html',contexto)


