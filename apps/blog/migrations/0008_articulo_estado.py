# Generated by Django 2.2.2 on 2019-09-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190902_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='estado',
            field=models.BooleanField(default='True'),
            preserve_default=False,
        ),
    ]
