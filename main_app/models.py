from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('pets_detail', kwargs={'pk': self.id})

class Nft(models.Model):
    collection = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    attributes = models.TextField(max_length=250)
    purchased = models.DateField()
    pets = models.ManyToManyField(Pet)
    def __str__(self):
        return f'{self.collection} {self.name}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'nft_id': self.id})
    
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    nft = models.ForeignKey(
        Nft,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']