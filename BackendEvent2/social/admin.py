from django.contrib import admin


# Register your models here.from django.contrib import admin
from .models import Notification, Avis, Favori

admin.site.register(Notification)
admin.site.register(Avis)
admin.site.register(Favori)
