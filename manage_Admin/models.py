from django.db import models

class Intervenants(models.Model):
    idInt = models.AutoField(primary_key=True)
    prenom = models.CharField(max_length=100, verbose_name="Prenom de l'intervenant", null=True, blank=True)
    nom = models.CharField(max_length=100, verbose_name="Nom de l'intervenant", null=True, blank=True)
    specialites = models.CharField(max_length=100, verbose_name="Spécialité de l'intervenant", null=True, blank=True)
    photo = models.ImageField(upload_to='Intervenants/',null=True, blank=True, verbose_name="Image Intervenant" )

    def __str__(self):
        return f"{self.prenom}- {self.nom}- {self.specialites}"

class Evenements(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100, verbose_name="Titre Evenement")
    description = models.CharField(max_length=250, verbose_name="Description")
    date = models.DateField(auto_now=False)
    idInt = models.ForeignKey(Intervenants, verbose_name="Id Intervenants", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.titre}-{self.date}"

class Interview(models.Model):
    evenement = models.ForeignKey(Evenements, verbose_name="Événement", on_delete=models.CASCADE)
    intervenant = models.ForeignKey(Intervenants, verbose_name="Intervenant", on_delete=models.CASCADE)


class Partenaires(models.Model):
    idPart= models.AutoField(primary_key=True)
    logo = models.ImageField(upload_to="Partenaires", verbose_name="Logo partenaires")

class Evenements_Partenaires(models.Model):
    evenement = models.ForeignKey(Evenements, verbose_name="Événement", on_delete=models.CASCADE)
    partenaire = models.ForeignKey(Partenaires, verbose_name="Partenaire", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["evenement", "partenaire"],
                name="unique_evenement_partenaire",
            )
        ]

