from django.contrib import admin

# Register your models here.
from .models import * 

class ejemplares(admin.ModelAdmin):
    list_filter = ("due_back","status")
    list_display = ("book_id","status","due_back","id")
    fieldsets = ((
        None,{'fields':('book','imprint','id')}

    ) , 
    ('availability', {'fields':('status','due_back')}))


class AdminAuthor(admin.ModelAdmin):
    list_display = ("first_name","last_name","date_of_birth","date_of_death")
    fields = ['first_name','last_name',('date_of_birth','date_of_death')]
    
    #se puede usar elemento exclude para excluir campos esto tendra mas efecto en los formularios

class adminTabular(admin.TabularInline):
    model = BookInstance
    extra = 0
class bookadmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [adminTabular]

admin.site.register(Book,bookadmin)
admin.site.register(Lenguage)
admin.site.register(Author,AdminAuthor)
admin.site.register(BookInstance,ejemplares)
admin.site.register(Genre)


