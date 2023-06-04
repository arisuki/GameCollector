from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='index'),
    path('games/<int:game_id>/', views.games_detail, name='detail'),
    path('games/<int:game_id>/add_note/', views.add_note, name='add_note'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    
    path('consoles/', views.ConsoleList.as_view(), name='consoles_index'),
    path('consoles/<int:pk>/', views.ConsoleDetail.as_view(), name='consoles_detail'),
    path('consoles/create/', views.ConsoleCreate.as_view(), name='consoles_create'),
    path('consoles/<int:pk>/update/', views.ConsoleUpdate.as_view(), name='consoles_update'),
    path('consoles/<int:pk>/delete/', views.ConsoleDelete.as_view(), name='consoles_delete'),
]