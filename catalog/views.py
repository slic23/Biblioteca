from django.shortcuts import render,HttpResponse
from .models import *
from django.views import generic 
from django.core.paginator import Paginator
import re 

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
    numero = request.session.get('numvisitas',0)
    numerovisitas = numero+1
    request.session['numvisitas'] = numerovisitas 
    contexto = {
        'numero_libros':num_libros,
        'numero_ejemplares': numero_ejemplares,
        'ejemplares_disponibles': ejemplares_disponibles,
        'numero_autores':numero_autores,
        'numero_generos':numero_generos,
        'palabrasEncontradas':palabra_numeroVeces,
        'visitas':numerovisitas

    }


    return render(request,'index.html',contexto)


class Listarlibros(generic.ListView):
    model = Book
    paginate_by = 4
    paginate_orphans = 1 # esto puede ser calculado dinamicamente, dependiendo del numero de objetos
    #necesito obtener el nombre del autor teniendo en cuenta que Book , Author es una ManyTomany 



class autor(generic.DetailView):
    model = Author
    template_name = "autor-detalle.html"

class autores(generic.ListView):
    model = Author
    paginate_by = 5
        
def calculadora(request,signoNumero = None):
    def suma(a,b):
        return a+b
    def resta(a,b):
        return abs(a-b) #modificar luego
    def division(a,b):
        return a//b # 
    def multiplicacion(a,b):
        return a*b  
    resultado = 0
    def resultado():
                try:
                    
                    consultaNumeros = request.session['Numeros']
                    condicion = request.session["condicion"]
                    if len(consultaNumeros)==2:
                        "buscar que condicion ha sido llamada a realizar  esa operacion"
                        print("Dentro del bucle issam ")

                        if condicion in operaciones:
                            print(f"Esto es condicion ==> {condicion}")
                            resultado = llamadaOperacion.get(condicion)(int(numeros[0]),int(numeros[1]))
                            print(f"Este es el resultado -> {resultado}")
                            del request.session['Numeros']
                            del request.session['condicion']
                            contexto["resultado"] = resultado

                except KeyError:
                    print("Esto mas tarde incluir aqui avisos con mensajes de warning")

    contexto = {}
    """
    Logica de la calculadora
    """
    operaciones = ['suma','resta','multiplicacion','division']
    llamadaOperacion = {'suma':suma,'resta':resta,'multiplicacion':multiplicacion,'division':division}

    if signoNumero is not  None:
        
        numeroLimpio = 0
        if re.search(r"\d", signoNumero):
            numeroLimpio = signoNumero
            numero =  request.session.get('calculadoraNumero',0)
            request.session['calculadoraNumero']= numeroLimpio
            arr = []
            numeros = request.session.get('Numeros', arr)
        #
            print(f"Esto es numeros::: {numeros}")
            print(f'Esto es el signoNumero: {signoNumero}')
            numeros = numeros + [numeroLimpio]
            request.session['Numeros'] = numeros 
          
            
            contexto['numero'] = numeroLimpio
            #del request.session["Numeros"] 
            resultado()
            
            
        else:
            condicion = request.session.get('condicion',"")
            request.session['condicion'] =  signoNumero
            print(f"esta es la condicion -----> {request.session['condicion']}")
            consultaNumeros = request.session['Numeros']
            resultado()

        
    return  render(request,'calculadora.html',contexto)



