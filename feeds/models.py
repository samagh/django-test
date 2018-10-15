from django.db import models
from PIL import Image
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

FOTO_SIZE = (240, 240)
ICONO_SIZE = (64, 64)
IMAGEN_FONDO_SIZE = (240,64)

@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)

# Create your models here.

class EstiloFicha(models.Model):
    nombre        = models.CharField(primary_key=True,max_length=100)
    icono         = models.ImageField(null=True,blank=True, upload_to=PathAndRename('./estilo/icono/'))
    texto_tamanyo = models.CharField(null=True,blank=True,max_length=32)
    fondo_imagen  = models.ImageField(null=True,blank=True, upload_to=PathAndRename('./estilo/imagen/'))
    fondo_color   = models.CharField(null=True,blank=True, max_length=7)

    class Meta:
        verbose_name        = 'Estilo-Ficha'
        verbose_name_plural = 'Estilo-Fichas'

    def save(self):
        super(EstiloFicha, self).save()

        if self.icono != None and self.icono.path.split('/')[-1] != 'no_icono.jpg':
            image = Image.open(self.icono)
            image = image.resize(ICONO_SIZE, Image.ANTIALIAS)
            image.save(self.icono.path)

        if self.fondo_imagen != None and self.fondo_imagen.path.split != 'no-imagen.jpg':
            image = Image.open(self.fondo_imagen)
            image = image.resize(IMAGEN_FONDO_SIZE, Image.ANTIALIAS)
            image.save(self.fondo_imagen.path)

    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.nombre

class Escritor(models.Model):
    nombre       = models.CharField(primary_key=True,max_length=100)
    foto         = models.ImageField(upload_to=PathAndRename('./fotos/'),default='./fotos/no_foto.jpg')
    bibliografia = models.TextField(blank=True)

    class Meta:
        verbose_name        = 'Escritor'
        verbose_name_plural = 'Escritores'

    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.nombre

    def save(self):
        super(Escritor, self).save()
        if self.foto.path.split('/')[-1] != 'no_foto.jpg':
            image = Image.open(self.foto)
            image = image.resize(FOTO_SIZE, Image.ANTIALIAS)
            image.save(self.foto.path)

class Tema(models.Model):
    nombre      = models.CharField(primary_key=True,max_length=100)
    descripcion = models.CharField(max_length=150)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)
    estilo      = models.ForeignKey(EstiloFicha,null=True, related_name='temas',on_delete=models.SET_NULL)

    class Meta:
        verbose_name        = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.nombre

class Categoria(models.Model):
    nombre      = models.CharField(primary_key=True,max_length=100)
    descripcion = models.CharField(max_length=150)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)
    tema        = models.ForeignKey(Tema,null=True,related_name='categorias',on_delete=models.SET_NULL)
    estilo      = models.ForeignKey(EstiloFicha, null=True, related_name='categorias', on_delete=models.SET_NULL)

    class Meta:
        verbose_name        = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.nombre

class Articulo(models.Model):
    nombre     = models.CharField(primary_key=True,max_length=100)
    resumen    = models.CharField(max_length=512)
    texto      = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified   = models.DateTimeField(auto_now=True)
    escritor   = models.ForeignKey(Escritor,null=True,related_name='articulos',on_delete=models.SET_NULL)
    categoria  = models.ForeignKey(Categoria,null=True,related_name='articulos',on_delete=models.SET_NULL)
    estilo     = models.ForeignKey(EstiloFicha,null=True,related_name='articulos',on_delete=models.SET_NULL)

    class Meta:
        verbose_name        = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.nombre

IMAGEN = "IMG"
VIDEO  = "MPG"
DOCUMENTO = "DOC"

TIPOS_ADJUNTO = (
    ( DOCUMENTO, "Documento"),
    ( IMAGEN, "Imagen"),
    ( VIDEO, "Video"),
)

class Adjunto(models.Model):
    nombre = models.CharField(primary_key=True,max_length=100)
    tipo = models.CharField(max_length=3, choices=TIPOS_ADJUNTO)
    file = models.FileField(upload_to='./adjuntos/')
    created_at = models.DateTimeField(auto_now_add=True)
    modified   = models.DateTimeField(auto_now=True)
    articulo = models.ForeignKey(Articulo,related_name='adjuntos',on_delete=models.CASCADE)

    class Meta:
        verbose_name        = 'Adjunto'
        verbose_name_plural = 'Adjuntos'
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
