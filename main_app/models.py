from django.db import models

# Create your models here.
class Nft(models.Model):
    collection = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    attributes = models.TextField(max_length=250)
    purchased = models.DateField()

    def __str__(self):
        return f'{self.collection} {self.name}'
    