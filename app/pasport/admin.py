from django.contrib import admin

from app.pasport.models import Pasport

class PasportAdmin(admin.ModelAdmin):
    list_display = ["id", "registration", "status"]

admin.site.register(Pasport, PasportAdmin)