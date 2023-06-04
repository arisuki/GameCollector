from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

TYPE = (
    ('T', 'Thoughts'),
    ('R', 'Review'),
    ('P', 'Progress')
)


class Console(models.Model):
    name = models.CharField(max_length=50)
    released = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('consoles_detail', kwargs={'pk': self.id})

class Game(models.Model):
    name = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)
    details = models.TextField(max_length=500)
    # consoles = models.ManyToManyField(Console)
    genre = models.CharField(max_length=50)
    released = models.IntegerField()

    def __str__(self):
        return f'{self.name}({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
    
    def posted_today(self):
        return self.note_set.filter(date=date.today())
    


class Note(models.Model):
    date = models.DateField('posted on', auto_now_add=True)
    content = models.CharField('content of note', max_length=500)
    type = models.CharField(
        'type of note',
        max_length=1,
        choices = TYPE,
        default=TYPE[0][0],
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.get_type_display()} on {self.date}"
    