from django.contrib import admin

# Register your models here.
from .models import Tarjetas
from .models import Marcas


admin.site.register(Tarjetas)
admin.site.register(Marcas)
