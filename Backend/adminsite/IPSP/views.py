from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from .models import *
import json
import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here
# .
#API de Eventos
def get_Eventos(request):
    if request.method=='GET':
        response = dict()
        data = Contacto.objects.all()
        id = request.GET.get("fecha")
        mesEvento = Mes_Evento.objects.get(mes=id)
        evento = Evento.objects.filter(mes = mesEvento.id_mes)
        contador =0 
        for e in evento:
            res = dict()
            contador = contador +1
            response["Evento " + str(contador)]=res
            res['day'] = e.fecha.day
            res['month'] = id
            res['year'] = e.fecha.year
            res['time'] = e.hora
            res['title'] = e.titulo
            res['desc'] = e.descripcion
            res['place']= e.lugar
    return JsonResponse(response)


#API de Servicios del directorio de empleados
def get_Contacto(request):
    if request.method=='GET':
        response = dict()
        data = Contacto.objects.all()
        contador = 0
        for contacto in data:
            res = dict()
            contador=contador+1
            response["Contacto "+ str(contador)]=res
            res["Nombre"]=contacto.nombre 
            res["Correo"]=contacto.correo
            res["Ubicacion"]=contacto.ubicacion
            res["Extension"]=contacto.extension

    return JsonResponse(response)


def get_Empleado(request):
    if request.method=='GET':
        response = dict()
        data = Empleado.objects.all()
        contador = 0
        today = datetime.date.today()

        month_number = today.month
        datetime_object = datetime.datetime.strptime(str(month_number), "%m")
        month_name = datetime_object.strftime("%b")

        for empleado in data:
            res = dict()
            contador=contador+1
            if(empleado.fecha_nacimiento.month==today.month):
                response["Empleado "+ str(contador)]=res
                res["name"]=empleado.nombre +'\t'+ empleado.apellido
                res["date"]=str(empleado.fecha_nacimiento.day) +" de "+ month_name
                res["image"]=empleado.imagen.url

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