from django.contrib import admin
from .models import Plant, Control, PlantType, Group

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass


@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    pass


@admin.register(PlantType)
class PlantTypeAdmin(admin.ModelAdmin):
    list_display = ("label", "sub_type", "owner", )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("label", "owner", )
