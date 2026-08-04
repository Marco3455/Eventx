# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Categorie)
admin.site.register(Entreprise)
admin.site.register(Lieu)
admin.site.register(Organisateur)
admin.site.register(Evenement)