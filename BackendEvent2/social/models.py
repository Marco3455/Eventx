from django.db import models

# Create your models here.
import uuid

from django.conf import settings
from django.db import models

from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)



# =====================================================
# NOTIFICATION
# =====================================================


class Notification(models.Model):


    class Type(models.TextChoices):

        SYSTEME = (
            "systeme",
            "Système"
        )

        RESERVATION = (
            "reservation",
            "Réservation"
        )

        PAIEMENT = (
            "paiement",
            "Paiement"
        )

        EVENEMENT = (
            "evenement",
            "Événement"
        )

        PROMOTION = (
            "promotion",
            "Promotion"
        )



    id = models.UUIDField(

        primary_key=True,

        default=uuid.uuid4,

        editable=False

    )


    utilisateur = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.PROTECT,

        related_name="notifications"

    )


    type = models.CharField(

        max_length=30,

        choices=Type.choices,

        default=Type.SYSTEME

    )


    titre = models.CharField(

        max_length=200

    )


    contenu = models.TextField()



    url_action = models.CharField(

        max_length=255,

        blank=True

    )



    lu = models.BooleanField(

        default=False

    )


    lu_le = models.DateTimeField(

        null=True,

        blank=True

    )


    cree_le = models.DateTimeField(

        auto_now_add=True

    )


    def __str__(self):

        return self.titre




# =====================================================
# AVIS
# =====================================================


class Avis(models.Model):


    id = models.UUIDField(

        primary_key=True,

        default=uuid.uuid4,

        editable=False

    )


    utilisateur = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.PROTECT,

        related_name="avis"

    )


    evenement = models.ForeignKey(

        "events.Evenement",

        on_delete=models.CASCADE,

        related_name="avis"

    )


    note = models.PositiveIntegerField(

        validators=[

            MinValueValidator(1),

            MaxValueValidator(5)

        ]

    )


    commentaire = models.TextField(

        blank=True

    )


    approuve = models.BooleanField(

        default=False

    )


    cree_le = models.DateTimeField(

        auto_now_add=True

    )


    modifie_le = models.DateTimeField(

        auto_now=True

    )



    class Meta:

        constraints = [

            models.UniqueConstraint(

                fields=[

                    "utilisateur",

                    "evenement"

                ],

                name="unique_avis_utilisateur_evenement"

            )

        ]



    def __str__(self):

        return f"{self.note}/5"





# =====================================================
# FAVORI
# =====================================================


class Favori(models.Model):


    id = models.UUIDField(

        primary_key=True,

        default=uuid.uuid4,

        editable=False

    )


    utilisateur = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.PROTECT,

        related_name="favoris"

    )


    evenement = models.ForeignKey(

        "events.Evenement",

        on_delete=models.CASCADE,

        related_name="favoris"

    )


    cree_le = models.DateTimeField(

        auto_now_add=True

    )



    class Meta:

        constraints = [

            models.UniqueConstraint(

                fields=[

                    "utilisateur",

                    "evenement"

                ],

                name="unique_favori_utilisateur_evenement"

            )

        ]



    def __str__(self):

        return f"{self.utilisateur} - {self.evenement}"