from django.shortcuts import render, redirect
from .models import Game, Console
from .forms import NoteForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    note_form = NoteForm()
    return render(request, 'games/detail.html', {'game': game, 'note_form': note_form})

class GameCreate(CreateView):
    model = Game
    fields = '__all__'

class GameUpdate(UpdateView):
    model = Game
    fields = '__all__'
    # ['finished', 'detail', 'console', 'genre', 'released' ]

class GameDelete(DeleteView):
    model = Game
    success_url = '/games'

def add_note(request, game_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.game_id = game_id
        new_note.save()
    return redirect('detail', game_id=game_id)


class ConsoleList(ListView):
  model = Console

class ConsoleDetail(DetailView):
  model = Console

class ConsoleCreate(CreateView):
  model = Console
  fields = '__all__'

class ConsoleUpdate(UpdateView):
  model = Console
  fields = ['name', 'released']

class ConsoleDelete(DeleteView):
  model = Console
  success_url = '/consoles'

