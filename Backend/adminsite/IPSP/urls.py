from django.urls import path
from .views import *
#from django.contrib.auth import logout
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('authentication/', agregarUsuariosToAuthentication,name="cambio"),
    path('deleteauth/', deleteAuth,name="deleteauth"),

    path('cambio/', LoginUser.as_view(),name="cambio"),
    path('login_frontend/', login_frontend),

    path('credenciales/', getCredentials),
    path('get_user/', get_userByName),

    path('get_brigada/', get_miembros_brigada),
    path('upadatePassUser/',postUpdatePassword),

      #Api Eventos
    path('getPrincipal/', get_Principal),

    #Api Buzon_Sugerencias
    path('postSugerencia/', postCreateSugerencia),
    path('postTipoSugerencia/', postCreateTipoSugerencia),
    path('getSugerencia/', get_Sugerencia),

    #Api Empleados
    path('getEmpleadoBirthday/', get_Empleado),
    path('getEmpleadoPorCedula/<str:pk>', get_empleadoPorCedula),


    #Api Empleados
    path('getContacto/', get_Contacto),
    path('postDataUser/', postUpdateEmpleado),

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
    path('registroBrigada/', view_RegistrarBrigada, name='brigada'),

    path('modificarPrincipal/', view_ModificarPrinciapl, name='modificar_principal'),



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

    path('modificarBrigada/', view_ModificarBrigada, name='modificar_brigada'),

    path('deleteEmpleado/', view_DeleteEmpleado, name='deletempleado'),
    path('deleteEmpleado/<str:pk>', delete_empleado, name='delete_empleado'),

    path('deleteCategoriaNoticia/', view_DeleteCategoriaNoticia, name='deletecategoria'),
    path('deleteCategoriaNoticia/<int:pk>', delete_categoriaNoticia, name='delete_categoriaNoticia'),
   
    path('deleteCategoriaBrigada/', view_DeleteCategoriaBrigada, name='delete_CategoriaBrigada'),
    path('deleteCategoriaBrigada/<int:pk>', delete_categoriaBrigada, name='delete_categoriaBrigada'),
    
   path('deleteLogrosEmpleados/',view_LogroEmpleado,name='logros'),
   path('deleteLogrosEmpleados/<int:pk>',delete_LogroEmpleado,name='logros'),


    path('deleteBrigada/', view_DeleteBrigada, name='deletebrigada'),

    path('buzon/',view_buzon,name='buzon'),

    path('', login, name='login'),
    path('logout/', logout_view, name='logout'),

    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),

    #recuperacion de clave de usuarios
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('sendEmail/', sendEmail),

    
]
