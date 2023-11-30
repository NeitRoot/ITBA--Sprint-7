from django.db import models
from cliente.models import Cliente
# # Create your models here.


class TipoDeCuenta(models.Model):
    type = models.TextField(blank=True, null=True)


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.ForeignKey(
        'TipoDeCuenta', models.DO_NOTHING, blank=True, null=True)
