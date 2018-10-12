from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import GameReview
from .models import Game

def game_list(request):
    game = Game.objects.all
    return render(request, 'gamedatabase/index.html', {'game': game})
