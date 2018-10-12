from django import forms
from .models import Game


class GameReview(forms.ModelForm):
    class Meta:
        model = Game
        fields = {'title', 'genre', 'rating', 'review', }
