from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# -*- coding: utf-8 -*-

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

    def save(self, *args, **kwargs):
        try:
            this = Evento.objects.get(id_evento=self.id_evento)
            if this.imagen != self.imagen:
                this.imagen.delete()
        except: 
            print("Ha ocurrido un error en actualizar la imagen")
            pass
        super(Evento, self).save(*args, **kwargs)

    def delete(self,*args,**kwargs):
        self.imagen.delete()
        super().delete(*args,**kwargs)



class Tipo_categoria(models.Model):
    id_tipocat = models.AutoField(primary_key=True )
    categoria = models.CharField(max_length=100)

class Empleado(models.Model):
    id_empleado = models.CharField(max_length=10,null=False)
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='auth_user')
    tipo_categoria = models.ForeignKey(Tipo_categoria, on_delete=models.CASCADE,null=True)
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    correo = models.CharField(max_length=300)
    rol = models.CharField(max_length=2,default='U')#A: administrador, U: usuario
    fecha_nacimiento =  models.DateField(blank=True, null=True)
    ubicacion = models.CharField(max_length=55,null=True)
    imagen = models.ImageField(verbose_name="Imagen",null=True )

    '''sobrescritura del metodo save de django para eliminar la imagen
    si esta se actualiza'''
    def save(self, *args, **kwargs):
        try:
            this = Empleado.objects.get(id_empleado=self.id_empleado)
            if this.imagen != self.imagen:
                this.imagen.delete()
        except: 
            print("Ha ocurrido un error en actualizar la imagen")
            pass
        super(Empleado, self).save(*args, **kwargs)    

    '''sobrescritura del metodo delete de django para eliminar la imagen'''
    def delete(self,*args,**kwargs):
        self.imagen.delete()
        super().delete(*args,**kwargs)


class Tipo_noticia(models.Model):
    id_tiponot = models.AutoField(primary_key=True )
    categoria = models.CharField(max_length=100)

class Principal(models.Model):
    id_principal = models.AutoField(primary_key=True )
    nombre_empresa = models.CharField(max_length=150)
    eslogan = models.CharField(max_length=190)
    image_eslogan = models.ImageField(verbose_name="Imagen")
    image_principal = models.ImageField(verbose_name="Imagen")

    def save(self, *args, **kwargs):
        try:
            this = Principal.objects.get(id_principal=self.id_principal)
            if this.image_eslogan != self.image_eslogan and this.image_principal != self.image_principal:
                this.image_eslogan.delete()
                this.image_principal.delete()
        except: 
            print("Ha ocurrido un error en actualizar la imagen")
            pass
        super(Principal, self).save(*args, **kwargs)    

class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    tipo_noticia = models.ForeignKey(Tipo_noticia, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=55)
    descripcion = models.TextField(max_length=550)
    fecha =  models.DateField(blank=True, null=True)
    imagen = models.ImageField(verbose_name="Imagen")

    def save(self, *args, **kwargs):
        try:
            this = Noticia.objects.get(id_noticia=self.id_noticia)
            if this.imagen != self.imagen:
                this.imagen.delete()
        except: 
            print("Ha ocurrido un error en actualizar la imagen")
            pass
        super(Noticia, self).save(*args, **kwargs)    

    def delete(self,*args,**kwargs):
        self.imagen.delete()
        super().delete(*args,**kwargs)

class Tipo_brigada(models.Model):
    id_tipobrigada = models.AutoField(primary_key=True )
    nombre_brigada = models.CharField(max_length=100)

class Brigada(models.Model):
    id_brigada = models.AutoField(primary_key=True)
    tipo_bri = models.ForeignKey(Tipo_brigada, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    miembro = models.TextField(max_length=200)
    imagen = models.ImageField(verbose_name="Imagen")
    
    def delete(self,*args,**kwargs):
        self.imagen.delete()
        super().delete(*args,**kwargs)

'''
class a18usuarios(models.Model):    
    cedula = models.CharField(max_length=10,primary_key=True,null=False)
    clave= models.CharField(max_length=100,null=True)
    nombres = models.CharField(max_length=200,null=True)
    apellidos = models.CharField(max_length=200,null=True)
    mail = models.CharField(max_length=200,null=True)
    tipo = models.CharField(max_length=100,default="Usuario")#Amdinistrador #Gestor
    estado = models.CharField(max_length=1,default="A")#A= Activo #I= Inactivo
    fecha_creacion =  models.DateField(blank=True, null=True)
    usuario_creacion =  models.CharField(max_length=100,null=True)
    fecha_modificaion =  models.DateField(blank=True, null=True)
    usuario_modificacion =  models.CharField(max_length=100,null=True)'''

class a18usuarios(models.Model):
    cedula = models.CharField(max_length=10,primary_key=True,null=False)
    clave= models.CharField(max_length=100,null=True)
    nombres = models.CharField(max_length=200,null=True)
    apellidos = models.CharField(max_length=200,null=True)
    mail = models.CharField(max_length=200,null=True)
    tipo = models.CharField(max_length=100,default="Usuario")#Amdinistrador #Gestor
    estado = models.CharField(max_length=1,default="A")#A= Activo #I= Inactivo
    fecha_crea =  models.DateField(blank=True, null=True)
    usuario_crea =  models.CharField(max_length=100,null=True)
    fecha_modi =  models.DateField(blank=True, null=True)
    usuario_modi =  models.CharField(max_length=100,null=True)
    class Meta:
       managed = True
       db_table = 'a18usuarios'


