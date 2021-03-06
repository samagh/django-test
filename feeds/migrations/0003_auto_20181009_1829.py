# Generated by Django 2.1.2 on 2018-10-09 18:29

from django.db import migrations, models
import feeds.models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20181009_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estiloficha',
            name='fondo_color',
            field=models.CharField(blank=True, max_length=7, null=True),
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
        migrations.AlterField(
            model_name='estiloficha',
            name='texto_tamanyo',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
