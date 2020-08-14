from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login as do_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import *
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.views import ObtainJSONWebToken
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response

# Create your views here
# .
def get_userByName(request):
    if request.method=='GET':
        response = dict()
        id= request.GET.get("id")#nombre
        print(id)
        user = User.objects.get(username=id)
        usuario = Empleado.objects.get(id_empleado=id)
        response["cedula"]=user.username
        response["nombre"]=usuario.nombre
        response["apellido"]=usuario.apellido
        response["correo"]=usuario.correo
        response["fecha"]=usuario.fecha_nacimiento
        #response["img"]=usuario.imagen.url
        print(user.first_name)

        return JsonResponse(response)


def get_Principal(request):
    data = Principal.objects.all()[0]
    res=dict()
    res["Empresa"]=data.nombre_empresa
    res["Eslogan"]=data.eslogan 
    res["Image_Eslogan"]=data.image_eslogan.url
    res["Image_Principal"]=data.image_principal.url
    return JsonResponse(res)


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
                res['resume']= noticia.descripcion[0:55]+" ..."
                res['date'] = datetime.datetime.strptime(str(noticia.fecha.month), "%m").strftime("%b")+" "+str(noticia.fecha.day)+", "+str(noticia.fecha.year)
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
            res['date'] = month_name+" "+str(noticia.fecha.day)+", "+str(noticia.fecha.year)
            res['image'] = noticia.imagen.url
            res['id'] = noticia.id_noticia
            res['cat'] = "Brigada de Seguridad"
    return JsonResponse(response)
def get_miembros_brigada(request):
    if request.method=='GET':
        response =dict()
        tipos_de_brigadas= Tipo_brigada.objects.all()
        for tipo in tipos_de_brigadas:
            brigadas= Brigada.objects.filter(tipo_bri=tipo.id_tipobrigada)
            res = dict()
            response[tipo.nombre_brigada]=res
            for miembros in brigadas:
                new = dict()
                res[miembros.id_brigada]=new
                new["miembro"]=miembros.miembro
                new["img"]=miembros.imagen.url
                new["brigada"]=tipo.nombre_brigada
    
    return JsonResponse(response)

def get_empleadoPorCedula(request,pk):
    if request.method=='GET':
        response = dict()
        print(pk)
        empleado =Empleado.objects.get(id_empleado=pk)
        response["Nombre"]=empleado.nombre
        response["Apellido"]=empleado.apellido
        response["Correo"]=empleado.correo
        response["Cedula"]=empleado.id_empleado
        response["User"]=empleado.auth_user.username
        response["Fecha"]=empleado.fecha_nacimiento
        response["Extension"]=empleado.ubicacion

    return JsonResponse(response)




def get_NoticiaPorCategoria(request):
    if request.method=='GET':
        response = dict()
        categorias = Tipo_noticia.objects.all()
        for categoria in categorias:
            noticias = Noticia.objects.filter(tipo_noticia = categoria.id_tiponot)#Codigo de Noticia Brigada
            res = dict()
            response[categoria.categoria]=res
            contador=0
            for noticia in noticias:
                new = dict()
                contador+=1
                res["contador"]=contador
                res[noticia.id_noticia] = new
                new['title'] = noticia.titulo
                new['descr'] = noticia.descripcion
                new['resume']= noticia.descripcion[0:55]+" ..."
                datetime_object = datetime.datetime.strptime(str(noticia.fecha.month), "%m")
                month_name = datetime_object.strftime("%b")
                new['date'] = month_name +" "+str(noticia.fecha.day)+", "+str(noticia.fecha.year)
                new['image'] = noticia.imagen.url
                new['cat'] = categoria.categoria
                new['id'] = noticia.id_noticia
    return JsonResponse(response)

def get_TodasLasNoticiasByID(request):
        if request.method=='GET':
            response = dict()
            id= request.GET.get("id")
            noticias = Noticia.objects.filter(tipo_noticia = id)
            contador =0 
            for noticia in noticias:
                res = dict()
                contador = contador +1
                response["Notica " + str(contador)]=res
                res['title'] = noticia.titulo
                res['descr'] = noticia.descripcion
                res['resume']= noticia.descripcion[0:55]+" ..."
                datetime_object = datetime.datetime.strptime(str(noticia.fecha.month), "%m")
                month_name = datetime_object.strftime("%b")
                res['date'] = month_name +" "+str(noticia.fecha.day)+", "+str(noticia.fecha.year)
                res['image'] = noticia.imagen.url
                res['id'] = noticia.id_noticia
                temp = Tipo_noticia.objects.get(id_tiponot=noticia.tipo_noticia_id)
                res['cat'] = temp.categoria
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
                res['resume']= noticia.descripcion[0:55]+" ..."
                datetime_object = datetime.datetime.strptime(str(noticia.fecha.month), "%m")
                month_name = datetime_object.strftime("%b")
                res['date'] = month_name +" "+str(noticia.fecha.day)+", "+str(noticia.fecha.year)
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
            res['date'] = str(noticia.fecha.month)+" "+str(noticia.fecha.day)+", "+str(noticia.fecha.year)
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
            res['image']=e.imagen.url
            res['time'] = e.hora
            res['title'] = e.titulo
            res['desc'] = e.descripcion
            res['place']= e.lugar
    return JsonResponse(response)


#API de Servicios del directorio de empleados
def get_Contacto(request):
    if request.method=='GET':
        response = dict()
        data = Empleado.objects.all()
        contador = 0
        for contacto in data:
            res = dict()
            contador=contador+1
            response["Contacto "+ str(contador)]=res
            res["Nombre"]=contacto.nombre + " " +contacto.apellido
            res["Correo"]=contacto.correo
            res["Extension"]="444"
            res["Ubicacion"]="Centro"

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
            if(empleado.fecha_nacimiento!=None and empleado.fecha_nacimiento.month==today.month):
                response["Empleado "+ str(contador)]=res
                res["name"]=empleado.nombre +'\t'+ empleado.apellido
                res["date"]=str(empleado.fecha_nacimiento.day) +" de "+ month_name
                if(bool(empleado.imagen)==True):
                    res["image"]=empleado.imagen.url

        return JsonResponse(response)

def get_MejorEmpleado(request):
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
                if(bool(empleado.imagen) == True):
                    res["image"]=empleado.imagen.url
                if(empleado.tipo_categoria!=None):
                    temp = Tipo_categoria.objects.get(id_tipocat=empleado.tipo_categoria_id)
                    res["MejorEn"]=temp.categoria
                    contador=contador+1
                    response["Empleado "+ str(contador)]=res
                    res["name"]=empleado.nombre +'\t'+ empleado.apellido
                    if(empleado.fecha_nacimiento !=None):
                        res["date"]=str(empleado.fecha_nacimiento.day) +" de "+ month_name
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
        ,sugerencia=response["sugerencia"],correo=response["correo"],ubicacion="No leido")
        sugerencia.save()
        return HttpResponse(status=200)
    return HttpResponse(status=404)

@csrf_exempt
def postUpdateEmpleado(request):
    if request.method=='POST':
        print("update")
        response = json.loads(request.body)
        empleado = Empleado.objects.get(id_empleado=response['id'])
        print(empleado)
        empleado.nombre=response["first_name"]
        empleado.apellido=response["last_name"]
        empleado.correo=response["mail"]
        print(response['mail'])
        empleado.ubicacion=response["extension"]
        empleado.fecha_nacimiento=response["fecha"]
        empleado.save()
        print("guardado")
        print(response['first_name'])
        #tipo = Tipo_sugerencia.objects.filter(sugerencia=response["tipo"])[0]
        #Aqui creo el elemento de tipo sugerencia
        return HttpResponse(status=200)
    return HttpResponse(status=404)
@csrf_exempt
def postUpdatePassword(request):
    if request.method=='POST':
        print("update")
        response = json.loads(request.body)
        auth = User.objects.get(username=response['id'])
        auth.set_password(response['password'])
        auth.save()
        empleado = Empleado.objects.get(id_empleado=response['id'])
        print(auth.first_name)
        print(response['password'])
        empleado.save()
        print(empleado.nombre)
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




#Vistas
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

@login_required(login_url='/')
@csrf_exempt
def view_RegistrarNoticias(request):
        response = Tipo_noticia.objects.all()
        print("registrando... noticias")
        if request.method=='POST':
            titulo = request.POST['titulo']
            fecha = request.POST['fecha']
            categoria = request.POST['categoria']
            imagen = request.FILES['archivoimg']
            descripcion = request.POST['descripcion']
            id_not = Tipo_noticia.objects.get(id_tiponot = categoria)
            noticia = Noticia(tipo_noticia_id=id_not.id_tiponot, titulo=titulo, descripcion=descripcion, fecha=fecha, imagen=imagen)
            noticia.save()
            print(titulo,fecha,categoria,imagen,descripcion)

        return render(request, 'views/views_register/register_noticia.html', {"categorias":response})

@login_required(login_url='/')
def view_RegistrarEventos(request):
        response = Mes_Evento.objects.all()
        if request.method=='POST':
            evento = request.POST['evento']
            fecha = request.POST['fecha']
            mes = request.POST['mes']
            lugar = request.POST['lugar']
            hora = request.POST['hora']
            imagen = request.FILES['imagen']
            descripcion = request.POST['descripcion'] 
            idfield = Mes_Evento.objects.filter(mes = mes)[0]
            mesEvento = Mes_Evento.objects.get(id_mes=idfield.id_mes)
            newEvento = Evento(titulo=evento,lugar=lugar,imagen=imagen,hora=hora,descripcion=descripcion,mes=mesEvento, fecha=fecha)
            newEvento.save()
            print(evento,fecha,mes,hora,lugar,imagen,descripcion)

        return render(request, 'views/views_register/register_evento.html', {"meses":response})

@login_required(login_url='/')
def view_RegistrarEmpleado(request):
    response= Tipo_categoria.objects.all()
    if request.method=='POST':
            nombre = request.POST['name']
            cedula = request.POST['cedula']
            apell = request.POST['apellido']
            usuario = request.POST['user']
            passwrd = request.POST['password']
            fecha = request.POST['fecha']
            correo = request.POST['correo']
            imagen = request.FILES['image']
            ext = request.POST['ext'] 
            mejorEn = request.POST['mejorEn'] 
            idfield = Tipo_categoria.objects.get(id_tipocat = mejorEn)
            auth5 = User.objects.create_user(
                username = usuario,
                password = passwrd,
                first_name=nombre, 
                last_name=apell,
                email=correo
            )
            empleado = Empleado(id_empleado=cedula,auth_user=auth5,
            tipo_categoria=idfield,nombre=nombre,apellido=apell,
            correo=correo,imagen=imagen,fecha_nacimiento=fecha,ubicacion=ext)
            empleado.save()
    return render(request, 'views/views_register/register_empleado.html', {"categorias":response})    

@login_required(login_url='/')
def view_ModificarPrinciapl (request):
    response= Principal.objects.all()[0]
    if request.method=='POST':
        print("entrando")
        principal = Principal.objects.get(id_principal=1)
        principal.nombre_empresa=request.POST['nombre_empresa']
        if(bool(request.FILES.get('image_principal', False)) == True ):
                principal.image_principal=request.FILES['image_principal']
        if(bool(request.FILES.get('image_eslogan', False)) == True ):
                principal.image_eslogan=request.FILES['image_eslogan']
        principal.eslogan=request.POST['eslogan']
        principal.save()
        response= Principal.objects.all()[0]

    return render(request, 'views/views_web/modify_index_web.html', {"Principal":response})

#'views/views_web/modify_index_web.html'
@login_required(login_url='/')
def view_RegistrarBrigada(request):
    response = Tipo_brigada.objects.all()
    if request.method=='POST':
            miembro_brigada = request.POST['miembro']
            imagen = request.FILES['archivoimg']
            tipo_brigada_ = request.POST['brigada_tipo']
            descripcion = request.POST['descripcion']
            id_bri = Tipo_brigada.objects.get(id_tipobrigada = tipo_brigada_)
            brigada = Brigada(tipo_bri=id_bri, miembro=miembro_brigada, descripcion=descripcion, imagen=imagen)
            brigada.save()
            print(miembro_brigada,tipo_brigada_,imagen,descripcion)
    return render(request, 'views/views_register/register_brigada.html', {"categorias":response})        
@login_required(login_url='/')
def view_ModificarBrigada(request):
    response = Brigada.objects.all()

    return render(request, 'views/views_modify/modify_brigada.html', {"brigadas":response})

@login_required(login_url='/')
def view_DeleteBrigada(request):
    response = Brigada.objects.all()
    return render(request, 'views/views_delete/delete_brigada.html', {"brigadas":response})        


@login_required(login_url='/')
def view_RegistrarCategoria(request):
    if request.method=='POST':
        if(request.POST.get("tipoForm1")=="form1"):
            tipo = Tipo_noticia(categoria=request.POST['tipoNoticia'])
            tipo.save()
        if(request.POST.get("tipoForm2")=="form2"):
            cate = Tipo_categoria(categoria=request.POST['categoria'])
            cate.save()
        if(request.POST.get("tipoForm3")=="form3"):
            brigada = Tipo_brigada(nombre_brigada=request.POST['categoria_brigada'])
            brigada.save()

    return render(request, 'views/views_register/register_categoria.html', {})    
@login_required(login_url='/')
def view_DeleteNoticia(request):
    response= Noticia.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(response, 4)
    try:
        notic = paginator.page(page)
    except PageNotAnInteger:
        notic = paginator.page(1)
    except EmptyPage:
        notic = paginator.page(paginator.num_pages)
    return render(request, 'views/views_delete/delete_noticia.html', {"listaNoticia":notic}) 

@login_required(login_url='/')
def delete_noticia(request, pk):
    val = pk
    noticia= Noticia.objects.get(id_noticia=val)
    noticia.delete()
    response= Noticia.objects.all()
    return render(request, 'views/views_delete/delete_noticia.html', {"listaNoticia":response}) 

@login_required(login_url='/')
def view_ModificarNoticia(request):
    response= Noticia.objects.all()
    return render(request, 'views/views_modify/modify_noticia.html', {"listaNoticia":response})

@login_required(login_url='/')
@csrf_exempt
def modificar_noticia(request,pk):#get noticia por id 
    print(pk)
    response= Noticia.objects.all()
    categoria = Tipo_noticia.objects.all()
    noticia= Noticia.objects.get(id_noticia=pk)
    cate_noticia=noticia.tipo_noticia
    print(noticia.titulo)
    print(noticia.imagen.url)
    print(noticia.fecha)
    print(noticia.descripcion)
    print(noticia.tipo_noticia.categoria)
    if request.method=='POST':
        noticia.titulo=request.POST['titulo']
        noticia.descripcion=request.POST['descripcion']
        if(request.POST['date']!=''):
            noticia.fecha=request.POST['date']
        if(bool(request.FILES.get('archivoimg', False)) == True ):
            print("Entrando...")
            noticia.imagen=request.FILES['archivoimg']
        tipo= Tipo_noticia.objects.get(id_tiponot=request.POST['categoria'])
        noticia.tipo_noticia=tipo
        noticia.save()
    return render(request, 'views/views_modify/modify_noticia.html', {"listaNoticia":response,"noticia":noticia,"categoria":categoria,"cate_noticia":cate_noticia}) 

@login_required(login_url='/')
def view_ModificarEvento(request):
    response= Evento.objects.all()
    return render(request,  'views/views_modify/modify_evento.html', {"listaEvento":response})

@login_required(login_url='/')
@csrf_exempt
def modificar_evento(request,pk):#get noticia por id 
    print(pk)
    response= Evento.objects.all()
    categoria = Tipo_noticia.objects.all()
    evento= Evento.objects.get(id_evento=pk)
    fecha =  str(evento.fecha.day)+"/"+ str(evento.fecha.month)+"/"+str(evento.fecha.year)
    print(fecha)
    if request.method=='POST':
        evento.titulo=request.POST['evento']
        evento.descripcion=request.POST['descripcion']
        print(request.POST['fecha']+"assssssssssd")
        if(request.POST['fecha']!=''):
            evento.fecha=request.POST['fecha']   
        if(bool(request.FILES.get('imagen', False)) == True ):
            evento.imagen=request.FILES['imagen']
        evento.hora=request.POST['hora']
        print(request.POST['hora'])
        evento.lugar=request.POST['lugar']
        evento.save()
    return render(request, 'views/views_modify/modify_evento.html', {"listaEvento":response,"evento":evento,"fechaevento":fecha}) 

@login_required(login_url='/')
def view_ModificarEmpleado(request):
    response = Empleado.objects.all()
    categoriaslist= Tipo_categoria.objects.all()

    return render(request, 'views/views_modify/modify_empleado.html', {"listaEmpleado":response,"categorias":categoriaslist})

@login_required(login_url='/')
@csrf_exempt
def modificar_empleado(request,pk):#get noticia por id 
    print(pk)
    response= Empleado.objects.all()
    categoriaslist = Tipo_categoria.objects.all()
    empleado= Empleado.objects.get(id_empleado=pk)
    if request.method=='POST':
        empleado.nombre=request.POST['name']
        empleado.apellido=request.POST['apellido']
        if(request.POST['fecha']!=''):
            empleado.fecha_nacimiento=request.POST['fecha']   
        if(request.POST['user']!=''):
            empleado.auth_user.username=request.POST['user']   
        if(request.POST['password']!=''):
            empleado.auth_user.password=request.POST['password']   
        if(request.POST['ext']!=''):
            empleado.ubicacion=request.POST['ext']
        if(bool(request.FILES.get('image', False)) == True ):
            empleado.imagen=request.FILES['image']
        if(request.POST['mejorEn']!=''):
            tip= Tipo_categoria.objects.get(id_tipocat=int(request.POST['mejorEn']))
            empleado.tipo_categoria = tip
        empleado.save()
    print("20000")
    return render(request,'views/views_modify/modify_empleado.html', {"listaEmpleado":response,"empleado":empleado,"categorias":categoriaslist}) 

@login_required(login_url='/')
def view_DeleteEvento(request):
    response= Evento.objects.all()
    return render(request, 'views/views_delete/delete_evento.html', {"listaEvento":response}) 

@login_required(login_url='/')
def delete_evento(request,pk):
    val = pk
    print(val)
    evento= Evento.objects.get(id_evento=pk)
    evento.delete()
    response= Evento.objects.all()
    return render(request, 'views/views_delete/delete_evento.html', {"listaEvento":response}) 
from django.contrib.auth.hashers import check_password

@login_required(login_url='/')
def view_DeleteEmpleado(request):
    response= Empleado.objects.all()
 

    return render(request, 'views/views_delete/delete_empleado.html', {"listaEmpleado":response}) 

@login_required(login_url='/')
def delete_empleado(request,pk):
    val = pk
    #empleado= Empleado.objects.get(id_empleado=val)
    #print(empleado.auth_user.id)
    #auth = User.objects.get(id=empleado.auth_user.id)
    #auth.delete()
    #empleado.delete()
    #print(val)
    
    response= User.objects.all()
    return render(request, 'views/views_delete/delete_empleado.html', {"listaEmpleado":response}) 

@login_required(login_url='/')
def view_DeleteCategoriaNoticia(request):
    response= Tipo_noticia.objects.all()
    response_brigadas= Tipo_brigada.objects.all()
    response_logros= Tipo_categoria.objects.all()

    return render(request, 'views/views_delete/delete_categorias.html', {"listaCategoriaNoticia":response,"logrosEmpleados":response_logros,"tiposBrigadas":response_brigadas}) 

@login_required(login_url='/')
def delete_categoriaNoticia(request,pk):
    val = pk
    tipo= Tipo_noticia.objects.get(id_tiponot=val)
    noticia = Noticia.objects.filter(tipo_noticia_id=tipo)
    noticia.delete()
    tipo.delete()
    response= Tipo_noticia.objects.all()
    return render(request, 'views/views_delete/delete_categorias.html', {"listaCategoriaNoticia":response}) 

@login_required(login_url='/')
def view_DeleteCategoriaBrigada(request):
    response_brigadas= Tipo_brigada.objects.all()
    return render(request, 'views/views_delete/delete_categoria_brigada.html', {"tiposBrigadas":response_brigadas}) 

@login_required(login_url='/')
def delete_categoriaBrigada(request,pk):
    val = pk
    tipo= Tipo_brigada.objects.get(id_tipobrigada=val)
    brigada = Brigada.objects.filter(tipo_bri=tipo)
    brigada.delete()
    tipo.delete()
    response= Tipo_brigada.objects.all()
    return render(request, 'views/views_delete/delete_categoria_brigada.html', {"tiposBrigadas":response}) 

@login_required(login_url='/')
def view_LogroEmpleado(request):
    response_logros= Tipo_categoria.objects.all()
    print(response_logros)
    return render(request, 'views/views_delete/delete_logros.html', {"tiposLogros":response_logros}) 

@login_required(login_url='/')
def delete_LogroEmpleado(request,pk):
    val = pk
    tipo= Tipo_categoria.objects.get(id_tipocat=val)
    empleado = Empleado.objects.filter(tipo_categoria=tipo)
    for emp in empleado:
        emp.tipo_categoria= None
        emp.save()       
    tipo.delete()
    response= Tipo_categoria.objects.all()
    return render(request, 'views/views_delete/delete_logros.html', {"tiposLogros":response}) 
    


@login_required(login_url='/')
@csrf_exempt
def view_buzon(request):
    buzon = Buzon_sugerencia.objects.all().order_by('-ubicacion')
    for i in buzon:
        print(i.id_sugerencia)
    page = request.GET.get('page', 1)
    paginator = Paginator(buzon, 20)
    try:
        buz = paginator.page(page)
    except PageNotAnInteger:
        buz = paginator.page(1)
    except EmptyPage:
        buz = paginator.page(paginator.num_pages)
    if request.method=='POST':
        print("entorsssss")
        bzn = Buzon_sugerencia.objects.get(id_sugerencia=request.POST['id_sugerencia'])
        bzn.ubicacion="Leido"
        bzn.save()
        buzon = Buzon_sugerencia.objects.all().order_by('-ubicacion')
        try:
             buz = paginator.page(page)
        except PageNotAnInteger:
            buz = paginator.page(1)
        except EmptyPage:
            buz = paginator.page(paginator.num_pages)
        print(buzon)
        return render(request,'views/views_web/buzon.html',{"lista":buz}) 

    return render(request,'views/views_web/buzon.html',{"lista":buz})

#'views/views_web/buzon.html'


from django.contrib.auth.backends import ModelBackend
from rest_framework import status

from django.contrib.auth import get_user_model
def agregarUsuariosToAuthentication(request):
        usuarios = a18usuarios.objects.all()
        for user in usuarios:
            #creo sus credenciales para la autenticacion
            
            if len(user.nombres)<30:
                auth = User.objects.create_user(
                            username = user.cedula,
                            password = user.clave,
                            email=user.mail,
                            first_name=user.nombres,
                            last_name=user.apellidos
                                
                )
                print(user)
                auth.save()
                empleado = Empleado(id_empleado=user.cedula,auth_user=auth,nombre=user.nombres,apellido=user.apellidos,
                correo=user.mail)
                empleado.save()
     

        print(usuarios[0])
        print("200 ok")
        return HttpResponse("hello!!!")
def deleteAuth(request):
        usuarios = User.objects.all()
        for user in usuarios:
                #creo sus credenciales para la autenticacion
            print(user)
            user.delete()
        print(usuarios[0])
        print("200 ok")
        return HttpResponse("hello!!!")


class EmailBackend(object):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
             user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        else:
            if getattr(user, 'is_active', False) and  user.check_password(password):
                return user
        return None
    def get_user(self, user_id):
        User = get_user_model()        
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

def getCredentials(request):
     if request.method=='GET':
        response = dict()
        id= request.GET.get("id")#nombre
        usuario = a18usuarios.objects.get(cedula=id)
        response["clave"]=usuario.clave
        print(usuario.clave)
        return JsonResponse(response)


def view_Login(request):
    print("hpla")
    login(request)
    return render(request, 'views/login/login.html', {})



# ...
@csrf_exempt
def login(request):
    # Creamos el formulario de autenticación vacío
    print("hola mundo")
    #user = authenticate(username="chjoguer", password='zywcCQAmPf')
   # print(user)
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        print(request.POST)
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            print(username)
            password = form.cleaned_data['password']
            print(password)
            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)
            print("verificando")

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                empleado =Empleado.objects.get(auth_user=user)
                print("si existe")
                # Y le redireccionamos a la portada
               # return redirect('registroNoticias/')
                return render(request, "views/views_register/register_noticia.html", {'nombre': empleado.nombre})

        else:
                print(form.is_valid())
                print("Password o usuario incorrecto")
                messages.error(request,"Usuario o password incorrectos. ")
                return render(request, "views/login/login.html", {'form': form,'mensaje':"Usuario o cotrnaseña iconrrecta."})


    # Si llegamos al final renderizamos el formulario
    return render(request, "views/login/login.html", {'form': form ,'mensaje':""})
from django.core.mail import EmailMessage, BadHeaderError, send_mail

@csrf_exempt
def sendEmail(request):
    if request.method == 'POST':
        response = json.loads(request.body)
        try:
            usuario = User.objects.get(email=response['correo'])
        except User.DoesNotExist:
            usuario = None
            print("No existe este elemetno...")
            return HttpResponse(status=404)

        print(response)
        print(usuario)
        new_password = User.objects.make_random_password()
        usuario.set_password(new_password)
        print(new_password)
        usuario.save()
        asunto = 'Cambio de contraseña de IPSP'
        mail = response['correo']
        mensaje = 'Usted ha solicitado recuperación de contraseña su contraseña nueva es la siguiente: '+ new_password
        nombres = 'Colaborador de Santa Priscila'

        if nombres != '' and len(mail.split('@')) == 2 and mensaje != '':
            textomensaje = '<br>'
            lista = mensaje.split('\n')
            c = 0
            for i in lista:
                textomensaje += i+'</br>'
                c+=1
                if len(lista)  > c :
                    textomensaje += '<br>'
            msj = '<p><strong>IPSP :</strong>'+nombres+'</p><p><strong>Correo: </strong>'+mail+'</p><strong>Mensaje: </strong>'+textomensaje+'</p>'
            msj2 = msj+'<br/><br/><br/><p>Usted se contacto con Industrial Pesquera Santa Priscila.</p><p><strong>NO RESPONDER A ESTE MENSAJE</strong>, nosotros nos pondremos en conacto con usted de ser necesario.</p><br/>'
            try:
                send_mail('Contactanos: '+asunto, msj,'ipspec2020@gmail.com', ['ipspec2020@gmail.com'], fail_silently=False, html_message = '<html><body>'+msj+'</body></html>')
                send_mail('Correo enviado: '+asunto, msj2, 'ipspec2020@gmail.com', [mail], fail_silently=False, html_message= '<html><body>'+msj2+'</body></html>')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Correo enviado',status=201)
    return HttpResponse(status=404)



def logout_view(request):
    logout(request)
    return redirect('/')

    # Redirect to a success page.

def error_404(request,exception=None):
    return render(request, "views/404.html",{})
@csrf_exempt
def login_frontend(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        print("verificando")

        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)
            print("verificando")

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                print("si existe")
                response_data = {
                #'es_admin_restaurante': user.es_admin_restaurante
                'token': "asdsad",
                }
                response = Response(data=response_data)
                # Y le redireccionamos a la portada
                return response

    # Si llegamos al final renderizamos el formulario
    return render(request, "views/login.html", {'form': form})

class LoginUser(ObtainJSONWebToken):
    print("XXXXXXXXXXXXXXXXXXXXXX")

    @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        #request.data  {'username': '___', 'password': '___'}
        print("yyyyyyyyyyyyyyyyyyyyy")

        serializer = self.get_serializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            user = serializer.object.get('username') or request.user
            token = serializer.object.get('token')
            print(user)
           # cedula=serializer.object.get('cedula')
           # token = serializer.object.get('token')
          #  empleado = Empleado.objects.get(id_empleado=cedula)
            #usuario = Usuarios.objects.get(id_usuario=user.id)
           # role_type = Roles.objects.get(id_rol = usuario.id_rol.id_rol)
            

            response_data = {
                 api_settings.JWT_AUTH_COOKIE: token,
                 'token':token,
                'username': "xyz",
                #'es_admin_restaurante': user.es_admin_restaurante
                #'typeUser': role_type.nombre,
            }
            response = Response(data=response_data)

            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE, token, expires=expiration, httponly=True)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
