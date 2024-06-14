from django.contrib import admin
from .models import Worker, Support

# Registrar el modelo Worker
admin.site.register(Worker)

# Registrar el modelo Support
admin.site.register(Support)
