# Generated by Django 4.2.7 on 2023-11-25 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_delete_cliente_delete_tipo_cliente'),
        ('sucursal', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sucursal',
        ),
    ]