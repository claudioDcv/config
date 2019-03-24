from django.contrib import admin
from .models import ElementSolution, Solution

@admin.register(ElementSolution)
class ElementSolutionAdmin(admin.ModelAdmin):
    list_display = ("label", "owner", )


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ("label", "owner", )
