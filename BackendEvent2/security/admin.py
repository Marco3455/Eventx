from django.contrib import admin
from .models import AuditLog, SessionUtilisateur

admin.site.register(AuditLog)
admin.site.register(SessionUtilisateur)
# Register your models here.
