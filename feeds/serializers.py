from rest_framework import serializers
from feeds.models import Escritor,Tema,Categoria,Articulo,Adjunto,EstiloFicha

# Serializers for Django Rest Framework
class EstiloFichaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = EstiloFicha
        fields = ('nombre','icono','texto_tamanyo','fondo_imagen','fondo_color')

class EscritorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Escritor
        fields = ('nombre','foto','bibliografia')


class AdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Adjunto
        fields = ('nombre','tipo','file','created_at','modified','articulo')

class ArticuloSerializer(serializers.ModelSerializer):
    adjuntos   = AdjuntoSerializer(many=True, read_only=True)
    estilo     = EstiloFichaSerializer(read_only=True)
    class Meta:
        model  = Articulo
        fields = ('nombre','resumen','texto','estilo','created_at','modified','escritor','categoria','adjuntos')

class CategoriaSerializer(serializers.ModelSerializer):
    articulos = ArticuloSerializer(many=True, read_only=True)
    estilo    = EstiloFichaSerializer(read_only=True)
    class Meta:
        model  = Categoria
        fields = ('nombre','descripcion','estilo','created_at','modified','tema','articulos')

class CategoriaOnlySerializer(serializers.ModelSerializer):
    estilo = EstiloFichaSerializer(read_only=True)
    class Meta:
        model  = Categoria
        fields = ('nombre','descripcion','estilo','created_at','modified','tema')


class TemaSerializer(serializers.ModelSerializer):
    estilo     = EstiloFichaSerializer(read_only=True)
    categorias = CategoriaOnlySerializer(many=True, read_only=True)
    class Meta:
        model  = Tema
        fields = ('nombre','descripcion','estilo','created_at','modified','categorias')
