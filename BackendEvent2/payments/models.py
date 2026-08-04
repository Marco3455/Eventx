from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
import uuid

from django.db import models



def generer_reference():

    code = uuid.uuid4().hex[:8].upper()

    return f"PAY-{code}"



class Paiement(models.Model):


    class Fournisseur(models.TextChoices):

        STRIPE = (
            "stripe",
            "Stripe"
        )

        PAYPAL = (
            "paypal",
            "PayPal"
        )

        PAYSTACK = (
            "paystack",
            "Paystack"
        )

        FLUTTERWAVE = (
            "flutterwave",
            "Flutterwave"
        )



    class Methode(models.TextChoices):

        CARTE = (
            "carte",
            "Carte bancaire"
        )


        MOBILE_MONEY = (
            "mobile_money",
            "Mobile Money"
        )

        MTN_MONEY = (
            "MTN_money",
            "MTN Money"
        )

        MOOV_MONEY = (
                    "MOOV_money",
                    "MOOV Money"
                )

        WAVE_MONEY = (
            "WAVE_money",
            "WAVE Money"
        )
        
        PAYPAL = (
            "paypal",
            "PayPal"
        )



    class Statut(models.TextChoices):

        EN_ATTENTE = (
            "en_attente",
            "En attente"
        )


        REUSSI = (
            "reussi",
            "Réussi"
        )


        ECHOUE = (
            "echoue",
            "Échoué"
        )


        REMBOURSE = (
            "rembourse",
            "Remboursé"
        )


        ANNULE = (
            "annule",
            "Annulé"
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



    commande = models.ForeignKey(

        'tickets.Commande',

        on_delete=models.PROTECT,

        related_name="paiements"

    )



    fournisseur = models.CharField(

        max_length=50,

        choices=Fournisseur.choices

    )



    methode = models.CharField(

        max_length=30,

        choices=Methode.choices

    )



    transaction_id = models.CharField(

        max_length=100,

        unique=True,

        null=True,

        blank=True

    )



    montant = models.DecimalField(

        max_digits=10,

        decimal_places=2

    )



    statut = models.CharField(

        max_length=20,

        choices=Statut.choices,

        default=Statut.EN_ATTENTE

    )



    ip_client = models.GenericIPAddressField(

        null=True,

        blank=True

    )



    user_agent = models.CharField(

        max_length=255,

        blank=True

    )



    paye_le = models.DateTimeField(

        null=True,

        blank=True

    )


    cree_le = models.DateTimeField(

        auto_now_add=True

    )


    modifie_le = models.DateTimeField(

        auto_now=True

    )



    def save(self,*args,**kwargs):

        if not self.reference:

            self.reference = generer_reference()


        super().save(*args,**kwargs)



    def __str__(self):

        return self.reference