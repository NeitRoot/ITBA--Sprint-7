from django.db import models
# from cuenta.models import Cuenta

from sucursal.models import Sucursal
from tarjeta.models import Tarjetas


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_dni = models.TextField(db_column='customer_DNI')
    dob = models.TextField(blank=True, null=True)
    branch = models.ForeignKey('sucursal.Sucursal', models.DO_NOTHING)
    card = models.ForeignKey('tarjeta.Tarjetas', models.DO_NOTHING)
