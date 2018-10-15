# Django Project Modelo

## Creacion de un modelo basico
models.py
``` python
from django.db import models

class Modelo(models.Model):
    # Declaramos uno como clave primaria
    nombre = models.CharField(primary_key=True, max_length=100)
    # Si no declararamos ninguna, crearia en la BBDD automaticamente uno como nombre 'id'
    # Cualquier CharField necesita un 'max_lenght'
    created = models.DateTimeField(auto_now_add=True)
    # Se inserta automaticamente la fecha en la Creacion
    modified = models.DateTimeField(auto_now=True)
    # Se modifica la fecha en cualquier modificacion
    ClaveAjena = models.ForeignKey(Tema,null=True,related_name='categorias',on_delete=models.SET_NULL)
    # Podemos declarar variables de otros Modelos, para relacionarlos com claves ajenas
    # Primer parametro, pasamos el Modelo del que es ClaveAjena, en este caso 'Tema'
    #   related_name = Nombre con el que se relaciona en el Modelo al que nos hemos linkado
    #   on_delete = Si borramos la referencia de la clave ajena, tipo de borrado de los que estan relacionados
    class Meta:
      verbose_name = 'Modelo'
      verbose_name_plural = 'Modelos'
    # Definimos el nombre que se mostrara en el administrador de django

    def __str__(self):
      return self.nombre
    # Texto que se mostrara en el Administrador de Django al referenciar al Objeto (Python 3)
    def __unicode__(self):
      return self.nombre
    # Texto que se mostrara en el Administrador de Django al referenciar al Objeto (Python 2)
```
## Administrador de Django

Registramos los modelos, para poder ser administrados en el **'admin.py'**
``` python
from django.contrib import admin
from project_name.models import Modelo

# Register your models here.
admin.site.register(Modelo)
```
Incluimos la ruta de administracion en **'urls.py'**
``` python
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
]
```
