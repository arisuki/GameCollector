from django.shortcuts import render

#usually a model is used
games = [
  {'name': 'The Legend of Zelda: A Link to the Past', 'console': 'Super Famicom', 'genre': 'action-adventure', 'released': '1991'},

  {'name': 'Chrono Trigger', 'console': 'Super Famicom', 'genre': 'JRPG', 'released': '1995'},

  {'name': 'Donkey Kong Country 3', 'console': 'Super Famicom', 'genre': 'platform', 'released': '1996'},
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    return render(request, 'games/index.html', {      'games': games
    })