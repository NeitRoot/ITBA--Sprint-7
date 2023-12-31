# Generated by Django 4.2.7 on 2023-11-29 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarjeta', '0001_initial'),
        ('sucursal', '0003_initial'),
        ('cliente', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarjetas',
            name='brand',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sucursal.sucursal'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tarjeta.tarjetas'),
        ),
        migrations.DeleteModel(
            name='Cuenta',
        ),
        migrations.DeleteModel(
            name='Marcas',
        ),
        migrations.DeleteModel(
            name='Sucursal',
        ),
        migrations.DeleteModel(
            name='Tarjetas',
        ),
        migrations.DeleteModel(
            name='TipoDeCuenta',
        ),
    ]
