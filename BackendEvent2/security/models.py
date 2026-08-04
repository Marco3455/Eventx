import uuid

from django.conf import settings
from django.db import models



# =====================================================
# JOURNAL DE SECURITE
# =====================================================

class AuditLog(models.Model):


    class Action(models.TextChoices):

        CREATE = (
            "create",
            "Création"
        )

        UPDATE = (
            "update",
            "Modification"
        )

        DELETE = (
            "delete",
            "Suppression"
        )

        LOGIN = (
            "login",
            "Connexion"
        )

        LOGOUT = (
            "logout",
            "Déconnexion"
        )

        PAYMENT = (
            "payment",
            "Paiement"
        )

        OTHER = (
            "other",
            "Autre"
        )



    id = models.UUIDField(

        primary_key=True,

        default=uuid.uuid4,

        editable=False

    )


    utilisateur = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="logs_securite"

    )


    action = models.CharField(

        max_length=30,

        choices=Action.choices

    )


    modele = models.CharField(

        max_length=100

    )


    objet_id = models.CharField(

        max_length=100

    )


    ancienne_valeur = models.JSONField(

        null=True,

        blank=True

    )


    nouvelle_valeur = models.JSONField(

        null=True,

        blank=True

    )


    adresse_ip = models.GenericIPAddressField(

        null=True,

        blank=True

    )


    user_agent = models.CharField(

        max_length=255,

        blank=True

    )


    cree_le = models.DateTimeField(

        auto_now_add=True

    )



    class Meta:

        ordering = [
            "-cree_le"
        ]



    def __str__(self):

        return f"{self.action} - {self.modele}"





# =====================================================
# SESSION UTILISATEUR
# =====================================================


class SessionUtilisateur(models.Model):


    id = models.UUIDField(

        primary_key=True,

        default=uuid.uuid4,

        editable=False

    )


    utilisateur = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE,

        related_name="sessions_securite"

    )


    # Hash du token JWT
    # Jamais stocker le token réel
    token_hash = models.CharField(

        max_length=255

    )


    adresse_ip = models.GenericIPAddressField()



    pays = models.CharField(

        max_length=100,

        blank=True

    )


    appareil = models.CharField(

        max_length=150,

        blank=True

    )


    navigateur = models.CharField(

        max_length=100,

        blank=True

    )


    active = models.BooleanField(

        default=True

    )


    derniere_activite = models.DateTimeField(

        auto_now=True

    )


    cree_le = models.DateTimeField(

        auto_now_add=True

    )



    def __str__(self):

        return str(self.utilisateur)