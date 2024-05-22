from django.contrib import admin
from .models import Filmovi


class FilmoviAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("naslov", )}


# Register your models here.
admin.site.register(Filmovi, FilmoviAdmin)
