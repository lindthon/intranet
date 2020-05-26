from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from .models import *
import json
import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here
# .
#Api de noticias 
def get_UltimaNoticias(request):
    if request.method=='GET':
        response = dict()
        noticiasAcutales = Noticia.objects.all()
        contador =0 
        today = datetime.date.today()
        temp =0
        for noticia in noticiasAcutales:
            res = dict()
            contador = contador +1
            if(noticia.fecha.month==today.month):
                response["Notica " + str(contador)]=res
                res['title'] = noticia.titulo
                res['descr'] = noticia.descripcion
                res['date'] = datetime.datetime.strptime(str(noticia.fecha.month), "%m").strftime("%b")+" "+str(noticia.fecha.day)
                res['image'] = noticia.imagen.url
                res['id'] = noticia.id_noticia
                temp = Tipo_noticia.objects.get(id_tiponot=noticia.tipo_noticia_id)
                res['cat'] = temp.categoria
    return JsonResponse(response)


def get_NoticiaBrigada(request):
    if request.method=='GET':
        response = dict()
        noticiaBrigada = Noticia.objects.filter(tipo_noticia = 1)#Codigo de Noticia Brigada
        contador =0 
        for noticia in noticiaBrigada:
            res = dict()
            contador = contador +1
            response["Notica " + str(contador)]=res
            res['title'] = noticia.titulo
            res['descr'] = noticia.descripcion
            datetime_object = datetime.datetime.strptime(str(noticia.fecha.month), "%m")
            month_name = datetime_object.strftime("%b")
            res['date'] = month_name+" "+str(noticia.fecha.day)
            res['image'] = noticia.imagen.url
            res['id'] = noticia.id_noticia
            res['cat'] = "Brigada de Seguridad"
    return JsonResponse(response)

def get_NoticiaPorCategoria(request):
    if request.method=='GET':
        response = dict()
        categorias = Tipo_noticia.objects.all()
        for categoria in categorias:
            noticias = Noticia.objects.filter(tipo_noticia = categoria.id_tiponot)#Codigo de Noticia Brigada
            res = dict()
            response[categoria.categoria]=res
            for noticia in noticias:
                new = dict()
                res[noticia.id_noticia] = new
                new['title'] = noticia.titulo
                new['descr'] = noticia.descripcion
                datetime_object = datetime.datetime.strptime(str(noticia.fecha.month), "%m")
                month_name = datetime_object.strftime("%b")
                new['date'] = month_name +" "+str(noticia.fecha.day)
                new['image'] = noticia.imagen.url
                new['cat'] = categoria.categoria
                new['id'] = noticia.id_noticia
    return JsonResponse(response)


def get_NoticiaByID(request):
        if request.method=='GET':
            response = dict()
            id= request.GET.get("id")
            noticiaBrigada = Noticia.objects.filter(id_noticia = id)
            contador =0 
            for noticia in noticiaBrigada:
                res = dict()
                contador = contador +1
                response["Notica " + str(contador)]=res
                res['title'] = noticia.titulo
                res['descr'] = noticia.descripcion
                datetime_object = datetime.datetime.strptime(str(noticia.fecha.month), "%m")
                month_name = datetime_object.strftime("%b")
                res['date'] = month_name +" "+str(noticia.fecha.day)
                res['image'] = noticia.imagen.url
                res['id'] = noticia.id_noticia
                temp = Tipo_noticia.objects.get(id_tiponot=noticia.tipo_noticia_id)
                res['cat'] = temp.categoria
        return JsonResponse(response)

def get_NoticiaCambiosPoliticos(request):
    if request.method=='GET':
        response = dict()
        noticiaBrigada = Noticia.objects.filter(tipo_noticia = 2)#Codigo de Noticia Cambios Politicos
        contador =0 
        for noticia in noticiaBrigada:
            res = dict()
            contador = contador +1
            response["Notica " + str(contador)]=res
            res['title'] = noticia.titulo
            res['descr'] = noticia.descripcion
            res['date'] = str(noticia.fecha.month)+" "+str(noticia.fecha.day)
            res['image'] = noticia.imagen.url
            res['id'] = noticia.id_noticia
            res['cat'] = "Cambios Politicos"
    return JsonResponse(response)

def get_CategoriaNoticia(request):
    if request.method=='GET':
        response=dict()
        categorias = Tipo_noticia.objects.all()
        contador = 0
        for categoria in categorias:
            res = dict()
            contador=contador+1
            response["Categoria "+ str(contador)]=res
            res["id"]=categoria.id_tiponot 
            res["categoria"]=categoria.categoria

    return JsonResponse(response)


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