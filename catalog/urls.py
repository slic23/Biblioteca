from django.urls import path 
from . import views
urlpatterns = [
  path('',views.index,name="index"),
  path('libros/',views.Listarlibros.as_view(),name="libros"),
  path('Author/<int:pk>/',views.autor.as_view(),name="Author"),
  path('Autores/',views.autores.as_view(),name="autores"),
  path('calculadora/<str:signoNumero>',views.calculadora, name="calculadora"),
  path('calculadora/',views.calculadora,name="calculadora"),
  path('registro-biblioteca/',views.Registro,name="registro"),
  path("prestados/",views.listadoPrestados.as_view(),name="prestados"),
  path("detalle-libro/<int:pk>/",views.detalleLibro.as_view(),name="detalle-libro"),
  path("todos-prestados/",views.LibrosPrestados.as_view(),name = 'allborrowed'),
  path("book/<uuid:pk>/renew", views.Librarian_renovar, name="renovar"),
  path("author/create", views.CrearAuthor.as_view() , name="crear-author"),
  path("eleminar/<int:pk>/Author",views.EleminarAuthor.as_view(),name="eleminar"),
  path("update/<int:pk>/Author",views.actualizarAuthor.as_view(),name = "update"),
  path("crear-libro/",views.CrearBook.as_view(),name="crearLibro"),
  path("eliminar/<int:pk>/libro",views.eleminarBook.as_view(),name="eleminarLibro"),
  path("actualizar/<int:pk>/libro",views.actualizarLibro.as_view(),name="actualizar")
]
