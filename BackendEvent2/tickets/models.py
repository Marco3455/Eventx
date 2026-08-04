import uuid

from django.conf import settings
from django.db import models



def generer_reference(prefix):

    code = uuid.uuid4().hex[:8].upper()

    return f"{prefix}-{code}"



# =====================================================
# TYPE BILLET
# =====================================================

class TypeBillet(models.Model):


    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


    public_id = models.CharField(
        max_length=30,
        unique=True,
        editable=False
    )


    evenement = models.ForeignKey(
        'events.Evenement',
        on_delete=models.CASCADE,
        related_name="types_billets"
    )


    nom = models.CharField(
        max_length=100
    )


    description = models.TextField(
        blank=True
    )


    prix = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    quantite_initiale = models.PositiveIntegerField(
        default=0
    )


    quantite_vendue = models.PositiveIntegerField(
        default=0
    )


    place_assignee = models.BooleanField(
        default=False
    )


    cree_le = models.DateTimeField(
        auto_now_add=True
    )



    def save(self,*args,**kwargs):

        if not self.public_id:

            self.public_id = generer_reference(
                "TYPE"
            )

        super().save(*args,**kwargs)



    @property
    def restant(self):

        return (
            self.quantite_initiale -
            self.quantite_vendue
        )



# =====================================================
# PLACE
# =====================================================


class Place(models.Model):


    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


    lieu = models.ForeignKey(
        'events.Lieu',
        on_delete=models.CASCADE,
        related_name="places"
    )


    section = models.CharField(
        max_length=50
    )


    rangee = models.CharField(
        max_length=10
    )


    numero = models.CharField(
        max_length=10
    )



    class Meta:

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "lieu",
                    "section",
                    "rangee",
                    "numero"
                ],

                name="unique_place_lieu"

            )

        ]



    def __str__(self):

        return f"{self.section}-{self.rangee}-{self.numero}"



# =====================================================
# COMMANDE
# =====================================================


class Commande(models.Model):


    class Statut(models.TextChoices):

        EN_ATTENTE = (
            "en_attente",
            "En attente"
        )

        PAYEE = (
            "payee",
            "Payée"
        )

        ANNULEE = (
            "annulee",
            "Annulée"
        )



    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


    reference = models.CharField(
        max_length=30,
        unique=True,
        editable=False
    )


    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="commandes"
    )


    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )


    statut = models.CharField(
        max_length=20,
        choices=Statut.choices,
        default=Statut.EN_ATTENTE
    )


    cree_le = models.DateTimeField(
        auto_now_add=True
    )


    modifie_le = models.DateTimeField(
        auto_now=True
    )



    def save(self,*args,**kwargs):

        if not self.reference:

            self.reference = generer_reference(
                "CMD"
            )

        super().save(*args,**kwargs)



# =====================================================
# BILLET
# =====================================================


class Billet(models.Model):


    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


    numero_serie = models.CharField(
        max_length=100,
        unique=True
    )


    commande = models.ForeignKey(
        Commande,
        on_delete=models.CASCADE,
        related_name="billets"
    )


    type_billet = models.ForeignKey(
        TypeBillet,
        on_delete=models.PROTECT,
        related_name="billets"
    )


    place = models.ForeignKey(
        Place,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="billets"
    )


    token_qr = models.CharField(
        max_length=255,
        unique=True
    )


    scanne = models.BooleanField(
        default=False
    )


    date_scan = models.DateTimeField(
        null=True,
        blank=True
    )


    statut = models.CharField(
        max_length=20,
        default="valide"
    )



# =====================================================
# PROMOTION
# =====================================================


class CodePromotionnel(models.Model):


    class TypeReduction(models.TextChoices):

        POURCENTAGE = (
            "pourcentage",
            "Pourcentage"
        )

        MONTANT = (
            "montant",
            "Montant fixe"
        )


    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


    code = models.CharField(
        max_length=30,
        unique=True
    )


    type_reduction = models.CharField(
        max_length=20,
        choices=TypeReduction.choices
    )


    reduction = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )


    utilisation_max = models.PositiveIntegerField(
        default=1
    )


    expire_le = models.DateTimeField(
        null=True,
        blank=True
    )