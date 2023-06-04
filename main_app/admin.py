from django.contrib import admin
from .models import Game, Note, Console

# Register your models here.
admin.site.register(Game)
admin.site.register(Note)
admin.site.register(Console)