from django.shortcuts import render, redirect
from .models import Game
from .forms import NoteForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
