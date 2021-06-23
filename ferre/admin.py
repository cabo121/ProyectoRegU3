from django.contrib import admin
from .models import manuales,neumaticas,electricas

model = manuales,neumaticas,electricas 

admin.site.register(model)