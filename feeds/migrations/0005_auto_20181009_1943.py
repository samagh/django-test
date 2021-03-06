# Generated by Django 2.1.2 on 2018-10-09 19:43

from django.db import migrations, models
import feeds.models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20181009_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjunto',
            name='file',
            field=models.FileField(upload_to='./adjuntos/'),
        ),
        migrations.AlterField(
            model_name='escritor',
            name='foto',
            field=models.ImageField(default='./fotos/no_foto.jpg', upload_to=feeds.models.PathAndRename('./fotos/')),
        ),
        migrations.AlterField(
            model_name='estiloficha',
            name='fondo_imagen',
            field=models.ImageField(blank=True, null=True, upload_to=feeds.models.PathAndRename('./estilo/imagen/')),
        ),
        migrations.AlterField(
            model_name='estiloficha',
            name='icono',
            field=models.ImageField(blank=True, null=True, upload_to=feeds.models.PathAndRename('./estilo/icono/')),
        ),
    ]
