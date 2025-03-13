from django.urls import path 
from . import views
urlpatterns = [
  path('',views.index,name="index"),
  path('libros/',views.Listarlibros.as_view(),name="libros"),
  path('Author/<int:pk>/',views.autor.as_view(),name="Author"),
  path('Autores/',views.autores.as_view(),name="autores"),
  path('calculadora/<str:signoNumero>',views.calculadora, name="calculadora"),
  path('calculadora/',views.calculadora,name="calculadora")

]