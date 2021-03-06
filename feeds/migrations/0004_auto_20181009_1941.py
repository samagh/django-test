# Generated by Django 2.1.2 on 2018-10-09 19:41

from django.db import migrations, models
import feeds.models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_auto_20181009_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjunto',
            name='file',
            field=models.FileField(upload_to='./static/adjuntos/'),
        ),
        migrations.AlterField(
            model_name='escritor',
            name='foto',
            field=models.ImageField(default='./static/fotos/no_foto.jpg', upload_to=feeds.models.PathAndRename('./images/fotos/')),
        ),
        migrations.AlterField(
            model_name='estiloficha',
            name='fondo_imagen',
            field=models.ImageField(blank=True, null=True, upload_to=feeds.models.PathAndRename('./static/estilo/imagen/')),
        ),
        migrations.AlterField(
            model_name='estiloficha',
            name='icono',
            field=models.ImageField(blank=True, null=True, upload_to=feeds.models.PathAndRename('./static/estilo/icono/')),
        ),
    ]
