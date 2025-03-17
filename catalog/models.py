from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200,help_text="Ingrese nombre el nombre del género (p. ej. Ciencia Ficción, Poesía Francesa etc.)) ", verbose_name="Genero")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de administración )
        """
        return self.name 
    





class Book(models.Model):
    """
    Modelo que representa un libro
    """

    title = models.CharField(max_length=50, verbose_name="Titulo")
    author = models.ManyToManyField('Author',blank=True, verbose_name="Autor")
    summary = models.TextField(max_length=1000,help_text="ingrese una breve descripcion del libro", verbose_name="sinopsis")
    isbn = models.CharField('ISBN',max_length=13,help_text="13 Caracteres <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>")
    Genre = models.ManyToManyField(Genre,blank=True)
    lenguaje = models.ForeignKey('Lenguage',null=True,blank=True, on_delete= models.CASCADE , verbose_name="Lenguaje original")
    """
        Es importante tener este dato por el cual se vera el numero de popularidad agrupado en los diferentes idiomas en que sea traducido. 
        la entidad traducción puede que mas tarde la define. 

    """

    def __str__(self):
        return self.title
    

    def ruta_particular_libro(self):
        """
            Esto devuelve la ruta de un libro en particular llamando a una url con un determinado name, pasandole su clave 

        """

        return reverse('detalle-libro', args=[str(self.id)])

    def ruta_del_autor(self):
        """
            Esto devuelve la ruta de un libro en particular llamando a una url con un determinado name, pasandole su clave 

        """

        return reverse('Author', args=[str(self.id)])


class BookInstance(models.Model):
    """
        Definiendo el ejemplar de cada libro. 
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="id unico para cada ejemplar")
    Lenguage = models.ManyToManyField('Lenguage',blank=True)
    book = models.ForeignKey(Book, null=False, on_delete= models.CASCADE , verbose_name="Libro")
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)
    LOAN_STATUS = (('m','Maintenence'),('o','On Loan'),('a','available'),('r','Reserved'))
    status = models.CharField(max_length=1,choices=LOAN_STATUS,default='m',blank=True , help_text="Disponibilidad del libro")

    class Meta:
        """
        Esto ordenara la salida de cualquier query de
        de una manera ordenada por la fecha en este caso de devolución desde la fecha más antigua a la mas reciente. 

        """
        ordering = ["due_back"]


    def __str__(self):
        return '%s %s' % (self.id,self.book.title)
    



class Author(models.Model):
    """
    un modelo que representa un autor
    
    """
    # sería una interesante funcionalidad averiguar la fecha de cumpleaños del autor y avisar al lector. 
    first_name = models.CharField('Nombre',max_length=100)
    last_name = models.CharField('Apellido',max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death = models.DateField('Died',null=True,blank=True)
    foto = models.ImageField(upload_to="ImagenesEscritores/", null=True)
    biografia = models.TextField(null=True,blank=True)
    
    def get_absolute_url(self):
        """
        Devolviendo la url de un autor en concreto. 
        
        """

        return reverse('Author',args=[str(self.pk)])
    

    def __str__(self):
        """
        como instancia de ese objeto, se hará hincapie que se identifique por su nombre , apellido
        """
        return '%s %s' % (self.first_name,self.last_name)
    
    


    """
        muchos autores escriben con seudonimos modificar mas tarde añadir una columna para ello  
        tambien establecer las fechas teniendo en cuenta  el peor caso,por ejemplo supongamos que quiero 
        meter a Homero, establecer las fechas por ahora se deja así (ejercicio para después) mirar B.C dates en python 

    """

class Lenguage(models.Model):
    """
        Este modelo tratara los diferentes lenguajes     
    """
    nombre = models.CharField('Lenguaje',max_length=20)

    def __str__(self):
        return self.nombre
    


class UsuarioBiblioteca(models.Model):
    """
    Este modelo tratra los datos del usuario estara enganchado con el usuario del sistema en una relacion de uno a uno
    """

    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    """
    Este null en password y repetir contraseña es por que lo introduci tarde y no podía borrar los datos 
    """
    password = models.CharField(max_length=100,verbose_name="Contraseña", default="1234")
    repetir = models.CharField(max_length=100,verbose_name="Vuelve a introducir contraseña", default="1234")
    apellidos = models.CharField(max_length=100,verbose_name="Apellidos")
    FechaNacimiento = models.DateField("Fecha Nacimiento", null=True)
    email = models.EmailField(verbose_name="Correo Electronico")
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE) #puedo tener usuarios sin capacidad para logearse 
    def __str__(self):
        return  f"{self.nombre} {self.apellidos}"

