from django.urls import path
from .views import *


urlpatterns = [

    #Api Buzon_Sugerencias
    path('postSugerencia/', postCreateSugerencia),
    path('postTipoSugerencia/', postCreateTipoSugerencia),
    path('getSugerencia/', get_Sugerencia),

    #Api Empleados
    path('getEmpleado/', get_Empleado),

]
