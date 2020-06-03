from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True )
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=55)
    extension = models.CharField(max_length=5)
    ubicacion = models.CharField(max_length=55)

class Tipo_sugerencia(models.Model):
    id_sug = models.AutoField(primary_key=True )
    sugerencia = models.CharField(max_length=100)

class Buzon_sugerencia(models.Model):
    id_sugerencia = models.AutoField(primary_key=True )
    tipo_sugerencia = models.ForeignKey(Tipo_sugerencia, on_delete=models.CASCADE)
    sugerencia = models.CharField(max_length=300)
    correo = models.CharField(max_length=65)
    ubicacion = models.CharField(max_length=55) 

class Mes_Evento(models.Model):
    id_mes = models.AutoField(primary_key=True )
    mes = models.CharField(max_length=55)
    mesCompleto = models.CharField(max_length=75)

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True )
    mes = models.ForeignKey(Mes_Evento, on_delete=models.CASCADE)
    fecha = models.DateField(blank=True, null=True)
    titulo = models.CharField(max_length=55)
    hora = models.CharField(max_length=55)
    descripcion = models.CharField(max_length=180)
    lugar = models.CharField(max_length=55)
    imagen = models.ImageField(verbose_name="Imagen")


class Tipo_categoria(models.Model):
    id_tipocat = models.AutoField(primary_key=True )
    categoria = models.CharField(max_length=100)

class Empleado(models.Model):
    id_empleado = models.CharField(max_length=55)
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='auth_user')
    tipo_categoria = models.ForeignKey(Tipo_categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=55)
    apellido = models.CharField(max_length=55)
    correo = models.CharField(max_length=75)
    fecha_nacimiento =  models.DateField(blank=True, null=True)
    ubicacion = models.CharField(max_length=55)
    imagen = models.ImageField(verbose_name="Imagen" )


class Tipo_noticia(models.Model):
    id_tiponot = models.AutoField(primary_key=True )
    categoria = models.CharField(max_length=100)


class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    tipo_noticia = models.ForeignKey(Tipo_noticia, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=55)
    descripcion = models.CharField(max_length=550)
    fecha =  models.DateField(blank=True, null=True)
    imagen = models.ImageField(verbose_name="Imagen")




