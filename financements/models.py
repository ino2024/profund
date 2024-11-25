from django.db import models

from django.db import models

class DemandeFinancement(models.Model):
    CIVILITE_CHOICES = [
        ('homme', 'Homme'),
        ('femme', 'Femme'),
        ('autre', 'Autre'),
    ]
    civilite = models.CharField(max_length=6, choices=CIVILITE_CHOICES)
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    pays = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    email = models.EmailField()
    adresse = models.CharField(max_length=255)
    revenu = models.DecimalField(max_digits=10, decimal_places=2)
    montant_financement = models.DecimalField(max_digits=10, decimal_places=2)
    projet = models.TextField()

    def __str__(self):
        return self.nom


class Contact(models.Model):
    name = models.CharField(max_length=255)  # Pour le champ Nom et Prénoms
    email = models.EmailField()  # Pour l'email
    subject = models.CharField(max_length=255)  # Pour le sujet
    message = models.TextField()  # Pour le message

    def __str__(self):
        return f"Message de {self.name} - Sujet: {self.subject}"