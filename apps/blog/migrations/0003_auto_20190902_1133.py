# Generated by Django 2.2.2 on 2019-09-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190902_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='descripcion',
            field=models.CharField(max_length=450, verbose_name='Descripción: '),
        ),
    ]
