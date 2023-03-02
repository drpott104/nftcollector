from django.db import models
from django.urls import reverse

# Create your models here.
class Nft(models.Model):
    collection = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    attributes = models.TextField(max_length=250)
    purchased = models.DateField()

    def __str__(self):
        return f'{self.collection} {self.name}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'nft_id': self.id})