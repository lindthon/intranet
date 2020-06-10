from django.urls import path
from .views import *
#from django.contrib.auth import logout


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
    path('getMejoresEmpleados/',get_MejorEmpleado),

    #Vistas
    path('registroNoticias/', view_RegistrarNoticias,name='noticia'),
    path('registroEventos/', view_RegistrarEventos,name='evento'),
    path('registroEmpleado/', view_RegistrarEmpleado, name='empleado'),
    path('registroCategorias/', view_RegistrarCategoria, name='categoria'),


    path('deleteEvento/', view_DeleteEvento, name='deletevento'),
    path('deleteEvento/<int:pk>', delete_evento, name='delete_evento'),

    path('deleteNoticia/', view_DeleteNoticia, name='delete'),
    path('deleteNoticia/<int:pk>', delete_noticia, name='delete_noticia'),

    path('modificarNoticia/', view_ModificarNoticia, name='modificar_noticia'),
    path('modificarNoticia/<int:pk>', modificar_noticia, name='modificarNoticia'),

    path('modificarEvento/', view_ModificarEvento, name='modificar_evento'),
    path('modificarEvento/<int:pk>', modificar_evento, name='modificarEvento'),


    path('modificarEmpleado/', view_ModificarEmpleado, name='modificar_empleado'),
    path('modificarEmpleado/<str:pk>',modificar_empleado, name='modificarEmpleado'),


    path('deleteEmpleado/', view_DeleteEmpleado, name='deletempleado'),
    path('deleteEmpleado/<int:pk>', delete_empleado, name='delete_empleado'),

    path('deleteCategoriaNoticia/', view_DeleteCategoriaNoticia, name='deletecategoria'),
    path('deleteCategoriaNoticia/<int:pk>', delete_categoriaNoticia, name='delete_categoriaNoticia'),

    
    path('', login, name='login'),
    path('logout/', logout_view, name='logout'),



    

]
