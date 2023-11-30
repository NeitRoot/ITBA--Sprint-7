from django.db import models

# Create your models here.


class Marcas(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)


class Tarjetas(models.Model):
    id_card = models.AutoField(primary_key=True)
    card_number = models.TextField()  # This field type is a guess.
    # Field name made lowercase. This field type is a guess.
    cvv = models.TextField(db_column='CVV')
    grant_date = models.TextField()
    expiration_date = models.TextField()
    card_type = models.TextField()
    brand = models.ForeignKey(Marcas, models.DO_NOTHING, blank=True, null=True)
