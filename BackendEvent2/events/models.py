import uuid

from django.conf import settings
from django.db import models
from django.utils.text import slugify


# =====================================================
# Générateurs d'identifiants publics
# =====================================================

def generer_public_id(prefix):

    code = uuid.uuid4().hex[:8].upper()

    return f"{prefix}-{code}"



# =====================================================
# CATEGORIE
# =====================================================

class Categorie(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


    nom = models.CharField(
        max_length=100,
        unique=True
    )


    slug = models.SlugField(
        unique=True,
        blank=True
    )


    icone = models.CharField(
        max_length=100,
        blank=True
    )


    actif = models.BooleanField(
        default=True
    )


    cree_le = models.DateTimeField(
        auto_now_add=True
    )


    modifie_le = models.DateTimeField(
        auto_now=True
    )



    def save(self,*args,**kwargs):

        if not self.slug:

            self.slug = slugify(self.nom)


        super().save(*args,**kwargs)



    def __str__(self):

        return self.nom



# =====================================================
# LIEU
# =====================================================

class Lieu(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


    nom = models.CharField(
        max_length=150
    )


    adresse = models.CharField(
        max_length=255
    )


    ville = models.CharField(
        max_length=100,
        db_index=True
    )


    pays = models.CharField(
        max_length=100
    )


    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )


    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )


    capacite = models.PositiveIntegerField(
        default=0
    )


    actif = models.BooleanField(
        default=True
    )


    cree_le = models.DateTimeField(
        auto_now_add=True
    )


    modifie_le = models.DateTimeField(
        auto_now=True
    )



    def __str__(self):

        return f"{self.nom} ({self.ville})"



# =====================================================
# ENTREPRISE
# =====================================================

class Entreprise(models.Model):

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


    nom = models.CharField(
        max_length=150
    )


    description = models.TextField(
        blank=True
    )


    logo = models.ImageField(
        upload_to="logos/",
        null=True,
        blank=True
    )


    site_web = models.URLField(
        blank=True
    )


    email = models.EmailField(
        blank=True
    )


    telephone = models.CharField(
        max_length=20,
        blank=True
    )


    verifie = models.BooleanField(
        default=False
    )


    cree_le = models.DateTimeField(
        auto_now_add=True
    )


    modifie_le = models.DateTimeField(
        auto_now=True
    )



    def save(self,*args,**kwargs):

        if not self.public_id:

            self.public_id = generer_public_id(
                "ENT"
            )


        super().save(*args,**kwargs)



    def __str__(self):

        return self.nom



# =====================================================
# ORGANISATEUR
# =====================================================

class Organisateur(models.Model):


    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


    utilisateur = models.OneToOneField(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE,

        related_name="organisateur_profile"

    )


    entreprise = models.ForeignKey(

        Entreprise,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="organisateurs"

    )


    biographie = models.TextField(
        blank=True
    )


    verifie = models.BooleanField(
        default=False
    )


    cree_le = models.DateTimeField(
        auto_now_add=True
    )


    modifie_le = models.DateTimeField(
        auto_now=True
    )



    def __str__(self):

        return self.utilisateur.email



# =====================================================
# EVENEMENT
# =====================================================

class Evenement(models.Model):


    class Statut(models.TextChoices):

        BROUILLON = (
            "brouillon",
            "Brouillon"
        )

        PUBLIE = (
            "publie",
            "Publié"
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


    public_id = models.CharField(

        max_length=30,

        unique=True,

        editable=False

    )


    categorie = models.ForeignKey(

        Categorie,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="evenements"

    )


    lieu = models.ForeignKey(

        Lieu,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="evenements"

    )


    proprietaire = models.ForeignKey(

        Organisateur,

        on_delete=models.PROTECT,

        related_name="evenements_crees"

    )


    organisateurs = models.ManyToManyField(

        Organisateur,

        related_name="evenements"

    )


    titre = models.CharField(

        max_length=200

    )


    slug = models.SlugField(

        unique=True,

        blank=True

    )


    description = models.TextField(

        blank=True

    )


    image_couverture = models.ImageField(

        upload_to="events/",

        null=True,

        blank=True

    )


    date_debut = models.DateTimeField()


    date_fin = models.DateTimeField()


    nombre_places = models.PositiveIntegerField(

        default=0

    )


    statut = models.CharField(

        max_length=20,

        choices=Statut.choices,

        default=Statut.BROUILLON

    )


    visible = models.BooleanField(

        default=False

    )


    publie_le = models.DateTimeField(

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


        if not self.public_id:

            self.public_id = generer_public_id(
                "EVENT"
            )


        if not self.slug:

            self.slug = slugify(
                self.titre
            )


        super().save(*args,**kwargs)



    def __str__(self):

        return self.titre