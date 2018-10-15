from django.shortcuts import render
from rest_framework import viewsets
# Cargamos los modelos
from feeds.models import Tema,Categoria,Articulo,Adjunto,Escritor
# cargamos los Serializers
from feeds.serializers import TemaSerializer,CategoriaSerializer,ArticuloSerializer,AdjuntoSerializer,EscritorSerializer

# Vies for Django Rest Framework
class TemaViewSet(viewsets.ModelViewSet):
    queryset = Tema.objects.all().order_by('-created_at')
    serializer_class = TemaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('-created_at')
    serializer_class = CategoriaSerializer

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all().order_by('-created_at')
    serializer_class = ArticuloSerializer

class EscritorViewSet(viewsets.ModelViewSet):
    queryset = Escritor.objects.all().order_by('-nombre')
    serializer_class = EscritorSerializer
