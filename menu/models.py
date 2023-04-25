from django.db import models


class Formation(models.Model):
    nom = models.CharField(max_length=500)
    description = models.TextField(max_length=10000)
    prix = models.IntegerField(default=0)

    def __str__(self):
        return self.nom
# Create your models here.
