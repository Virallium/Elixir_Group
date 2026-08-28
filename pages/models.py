from django.db import models

class Actualites(models.Model):
    titre = models.CharField(max_length=100, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    date_publiee = models.DateField(auto_now=True)
    source = models.CharField(verbose_name="source")#models avec link pour lire les liens
    def __str__(self):
        return self.titre

class Analyses(models.Model):
    note = models.IntegerField(verbose_name="Analyser")
    def __str__(self):
        return self.note

class Publication(models.Model):
    photo = models.ImageField(upload_to='Publication') 
    titre = models.CharField(verbose_name='Titre', max_length=25)
    description = models.TextField(verbose_name='Description', max_length=100)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.titre}- {self.date}"

class Opportunites(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100, verbose_name="Titre Opportunité")
    description = models.CharField(max_length=250, verbose_name="Description")
    date = models.DateField(auto_now=False)
    def __str__(self):
        return f"{self.titre}-{self.date}"