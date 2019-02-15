from django.contrib import admin
from .models import Plant, Control

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass


@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    pass
