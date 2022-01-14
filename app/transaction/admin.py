from django.contrib import admin

from app.transaction.models import Transaction, Music

admin.site.register(Transaction)
admin.site.register(Music)