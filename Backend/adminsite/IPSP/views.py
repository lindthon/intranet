from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login as do_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


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
                res['resume']= noticia.descripcion[0:6]
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
                contador=contador+1
                response["Empleado "+ str(contador)]=res
                res["name"]=empleado.nombre +'\t'+ empleado.apellido
                res["date"]=str(empleado.fecha_nacimiento.day) +" de "+ month_name
                res["image"]=empleado.imagen.url
                temp = Tipo_categoria.objects.get(id_tipocat=empleado.tipo_categoria_id)
                res["MejorEn"]=temp.categoria
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



#Vistas
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

@login_required
@csrf_exempt
def view_RegistrarNoticias(request):
        response = Tipo_noticia.objects.all()
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

        return render(request, 'viewRegistroNoticias.html', {"categorias":response})

@login_required
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

        return render(request, 'views/viewRegistroEventos.html', {"meses":response})


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
    return render(request, 'views/viewRegistroEmpleado.html', {"categorias":response})        

def view_RegistrarCategoria(request):
    if request.method=='POST':
        if(request.POST.get("tipoForm1")=="form1"):
            tipo = Tipo_noticia(categoria=request.POST['tipoNoticia'])
            tipo.save()
        if(request.POST.get("tipoForm2")=="form2"):
            cate = Tipo_categoria(categoria=request.POST['categoria'])
            cate.save()

    return render(request, 'views/viewRegistroCategoria.html', {})    
    
def view_DeleteNoticia(request):
    response= Noticia.objects.all()
    return render(request, 'views/viewDeleteNoticia.html', {"listaNoticia":response}) 

def delete_noticia(request, pk):
    val = pk
    noticia= Noticia.objects.get(id_noticia=val)
    noticia.delete()
    response= Noticia.objects.all()
    return render(request, 'views/viewDeleteNoticia.html', {"listaNoticia":response}) 

def view_ModificarNoticia(request):
    response= Noticia.objects.all()
    return render(request, 'views/viewModificarNoticia.html', {"listaNoticia":response})
@csrf_exempt
def modificar_noticia(request,pk):#get noticia por id 
    print(pk)
    response= Noticia.objects.all()
    categoria = Tipo_noticia.objects.all()
    noticia= Noticia.objects.get(id_noticia=pk)
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
    return render(request, 'views/viewModificarNoticia.html', {"listaNoticia":response,"noticia":noticia,"categoria":categoria}) 

def view_ModificarEvento(request):
    response= Evento.objects.all()
    return render(request, 'views/viewModificarEvento.html', {"listaEvento":response})
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
    return render(request, 'views/viewModificarEvento.html', {"listaEvento":response,"evento":evento,"fechaevento":fecha}) 

def view_ModificarEmpleado(request):
    response = Empleado.objects.all()
    return render(request, 'views/viewModificarEmpleado.html', {"listaEmpleado":response})

@csrf_exempt
def modificar_empleado(request,pk):#get noticia por id 
    print(pk)
    response= Empleado.objects.all()
    categoria = Tipo_categoria.objects.all()
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
        empleado.save()
    return render(request, 'views/viewModificarEmpleado.html', {"listaEmpleado":response,"empleado":empleado}) 

def view_DeleteEvento(request):
    response= Evento.objects.all()
    return render(request, 'views/viewDeleteEvento.html', {"listaEvento":response}) 


def delete_evento(request,pk):
    val = pk
    evento= Evento.objects.get(id_evento=val)
    evento.delete()
    response= Evento.objects.all()
    return render(request, 'views/viewDeleteEvento.html', {"listaEvento":response}) 

def view_DeleteEmpleado(request):
    response= Empleado.objects.all()
    return render(request, 'views/viewDeleteEmpleado.html', {"listaEmpleado":response}) 

def delete_empleado(request,pk):
    val = pk
    empleado= empleado.objects.get(id_empleado=val)
    empleado.delete()
    response= Evento.objects.all()
    return render(request, 'views/viewDeleteEmpleado.html', {"listaEmpleado":response}) 

def view_DeleteCategoriaNoticia(request):
    response= Tipo_noticia.objects.all()
    return render(request, 'views/viewDeleteCategoriaNoticia.html', {"listaCategoriaNoticia":response}) 

def delete_categoriaNoticia(request,pk):
    val = pk
    tipo= Tipo_noticia.objects.get(id_tiponot=val)
    noticia = Noticia.objects.filter(tipo_noticia_id=tipo)
    noticia.delete()
    tipo.delete()
    response= Tipo_noticia.objects.all()
    return render(request, 'views/viewDeleteCategoriaNoticia.html', {"listaCategoriaNoticia":response}) 


def view_Login(request):
    login(request)
    return render(request, 'views/login.html', {})



# ...
@csrf_exempt
def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)
            print("verificando")

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                print("si existe")
                # Y le redireccionamos a la portada
                return redirect('registroNoticias/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "views/login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')

    # Redirect to a success page.
