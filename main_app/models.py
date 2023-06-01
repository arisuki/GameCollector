from django.db import models
from django.urls import reverse

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)
    details = models.TextField(max_length=500)
    console = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    released = models.IntegerField()


    def __str__(self):
        return f'{self.name}({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
