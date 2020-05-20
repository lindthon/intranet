from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from .models import *
import json

from django.views.decorators.csrf import csrf_exempt

# Create your views here
# .
#API de Servicios del directorio de empleados
def get_Empleado(request):
    if request.method=='GET':
        response = dict()
        data = Empleado.objects.all()
        contador = 0
        for empleado in data:
            res = dict()
            contador=contador+1
            response["Empleado "+ str(contador)]=res
            res["Nombre "]=empleado.nombre
            res["Apellido "]=empleado.apellido
            res["Ubicaion"]=empleado.ubicacion
    return JsonResponse(response)



#API de Servicios de sugerencias
@csrf_exempt
def postCreateTipoSugerencia(request):
    if request.method=='POST':
        response = json.loads(request.body)
        #Aqui creo el elemento de tipo sugerencia
        tipo = Tipo_sugerencia(sugerencia=response["nuevaSugerencia"])
        tipo.save()
        return HttpResponse(status=200)
    return HttpResponse(status=404)


@csrf_exempt
def postCreateSugerencia(request):
    if request.method=='POST':
        response = json.loads(request.body)

        tipo = Tipo_sugerencia.objects.filter(sugerencia=response["tipo"])[0]
        #Aqui creo el elemento de tipo sugerencia
        sugerencia = Buzon_sugerencia(tipo_sugerencia=tipo
        ,sugerencia=response["sugerencia"],correo=response["correo"])

       
        sugerencia.save()
        return HttpResponse(status=200)
    return HttpResponse(status=404)
    
def get_Sugerencia(request):
    if request.method=='GET':
        response = dict()
        data = Buzon_sugerencia.objects.all()
        contador = 0
        for sugerencias in data:
            res = dict()
            contador=contador+1
            response["Sugerencias "+ str(contador)]=res
            suges=sugerencias.tipo_sugerencia
            res["Tipo Sugerencia"]=suges.sugerencia
            res["Descripcion"]=sugerencias.sugerencia
            res["Correo"]=sugerencias.correo
    return JsonResponse(response)

    print(tipo = Tipo_sugerencia.objects.filter(sugerencia=response["tipo"])[0])