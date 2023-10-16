from django.contrib import admin
from .models import Medicine,IssuedMedicine

# Register your models here.

admin.site.register(Medicine)
admin.site.register(IssuedMedicine)
