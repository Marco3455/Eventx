from django.db import models
import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Génération de l'identifiant public
def generer_public_id():
    code = uuid.uuid4().hex[:8].upper()
    return f"USER-{code}"



# Manager personnalisé pour email comme identifiant
class UtilisateurManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("L'email est obligatoire")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user


    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)


        return self.create_user(
            email,
            password,
            **extra_fields
        )



# Table Role
class Role(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    nom = models.CharField(
        max_length=50,
        unique=True
    )


    cree_le = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.nom



# Table Utilisateur
class Utilisateur(AbstractUser):


    # Ajout du manager personnalisé
    objects = UtilisateurManager()


    # UUID interne sécurisé
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


    # Suppression du username Django
    username = None



    # Identifiant visible par le frontend
    public_id = models.CharField(
        max_length=30,
        unique=True,
        editable=False
    )



    email = models.EmailField(
        unique=True
    )



    telephone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )



    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True
    )



    email_verifie = models.BooleanField(
        default=False
    )



    compte_bloque = models.BooleanField(
        default=False
    )



    roles = models.ManyToManyField(
        Role,
        related_name="utilisateurs",
        blank=True
    )



    cree_le = models.DateTimeField(
        auto_now_add=True
    )



    modifie_le = models.DateTimeField(
        auto_now=True
    )



    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []



    def save(self, *args, **kwargs):

        if not self.public_id:

            self.public_id = generer_public_id()


        super().save(*args, **kwargs)



    def __str__(self):

        return self.public_id