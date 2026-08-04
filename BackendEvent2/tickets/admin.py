# Register your models here.
from django.contrib import admin
from .models import Commande, Billet, Place, TypeBillet, CodePromotionnel

admin.site.register(Commande)
admin.site.register(Billet)
admin.site.register(Place)
admin.site.register(TypeBillet)
admin.site.register(CodePromotionnel)