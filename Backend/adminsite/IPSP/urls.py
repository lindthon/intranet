from django.urls import path
from .views import *


urlpatterns = [

    #Api Buzon_Sugerencias
    path('postSugerencia/', postCreateSugerencia),
    path('postTipoSugerencia/', postCreateTipoSugerencia),
    path('getSugerencia/', get_Sugerencia),

    #Api Empleados
    path('getEmpleadoBirthday/', get_Empleado),

    #Api Empleados
    path('getContacto/', get_Contacto),

     #Api Eventos
    path('getEvento/', get_Eventos),

  #Api Noticias
    path('getNoticiasBrigada/',get_NoticiaBrigada),
    path('getNoticiasCambio/',get_NoticiaCambiosPoliticos),
    path('getCategoria/',get_CategoriaNoticia),
    path('getUltimasNoticias/',get_UltimaNoticias),
    path('getNoticiasPorCategoria/',get_NoticiaPorCategoria),
    path('getNoticiasByID/',get_NoticiaByID),
    path('getTodasLasNoticiasByID/',get_TodasLasNoticiasByID),


    

]
