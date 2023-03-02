from django.db import models
# from django.db import reverse

# Create your models here.
class Nft(models.Model):
    collection = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    attributes = models.TextField(max_length=250)
    datePurchased = models.DateField()

    def __str__(self):
        return f'{self.collection} {self.name}'