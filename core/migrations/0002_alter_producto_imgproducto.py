# Generated by Django 3.2.4 on 2021-07-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imgProducto',
            field=models.ImageField(default='core/sin-imagen.jpg', upload_to='core', verbose_name='Imagen del producto'),
        ),
    ]
