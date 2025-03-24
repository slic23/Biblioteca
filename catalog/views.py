from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import *
from django.views import generic 
from django.core.paginator import Paginator
import re 
from .forms import registrobibli
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

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




def Registro(request):
    """
    Formulario de registro
    
    """

    if request.method == "POST":
        form = registrobibli(request.POST)
        if form.is_valid():
            nombre_form =  form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellidos"]
            contras = form.cleaned_data["password"]
            repcontras = form.cleaned_data["repetir"]
            fecha = form.cleaned_data["FechaNacimiento"]
            email_form = form.cleaned_data["email"]
            
            usuario = User.objects.create_user(username = nombre_form, password = repcontras , email = email_form)
            #usuario.save()
            usuario2 = UsuarioBiblioteca(nombre = nombre_form,password = contras, repetir = repcontras,apellidos = apellido, FechaNacimiento = fecha , email = email_form , user = usuario) 
            usuario2.save()
            return HttpResponseRedirect(reverse('index'))
    else:
       form = registrobibli()
    contexto = {
        'form':form
   }
    
    #print(form)
    
    return render(request,'registrobiblio.html',contexto)
    
    
    
class listadoPrestados(LoginRequiredMixin,generic.ListView):
    "Libros que ha tomado prestado el usuario"
    
    model = BookInstance
    template_name = "prestados.html"
    
    def get_queryset(self):
        print(self.request.user)
        print(f"Este es el pk del usuario {self.request.user.id}")
        return BookInstance.objects.filter(prestado__nombre = self.request.user).filter(status__exact = "o").order_by("due_back")
        
        
        
        
class detalleLibro(generic.DetailView):
    model = Book
    template_name = "detalle-libro.html"
    
        
        