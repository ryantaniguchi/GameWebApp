from django import forms
from .models import Game

# Form used to add new games to the database
class CreateNewGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["BGGId", "Name", "AvgRating", "NumRatings", "Playtime", "Thematic", "Strategy", "War", "Family", "CGS", "Abstract", "Party", "Child"]
        labels = {"BGGId": "BGGID", "Name": "Game Name", "AvgRating": "Average Rating", "NumRatings": "Number of Ratings", "Playtime": "Playtime", "Thematic": "Thematic", "Strategy": "Strategy Game", "War":"War Game", "Family":"Family Game", "CGS":"CGS Game", "Abstract":"Abstract Game", "Party":"Party Game", "Childrens":"Children's Game"}

class GameData(forms.Form):
    class meta:
        model = Game
        fields = '__all__'

