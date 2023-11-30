from django.contrib import admin

# Register your models here.
from .models import Cuenta
from .models import TipoDeCuenta


admin.site.register(Cuenta)
admin.site.register(TipoDeCuenta)
