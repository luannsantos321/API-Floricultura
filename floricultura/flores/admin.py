from django.contrib import admin
from .models import Flor


@admin.register(Flor)
class FlorAdmin(admin.ModelAdmin):
    pass
