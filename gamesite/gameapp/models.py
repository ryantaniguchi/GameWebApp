from django.db import models

class Game(models.Model):
    BGGId = models.IntegerField()
    Name = models.CharField(max_length=200)
    AvgRating = models.FloatField()
    NumRatings = models.IntegerField()
    Playtime = models.IntegerField()
    Thematic = models.BooleanField()
    Strategy = models.BooleanField()
    War = models.BooleanField()
    Family = models.BooleanField()
    CGS = models.BooleanField()
    Abstract = models.BooleanField()
    Party = models.BooleanField()
    Child = models.BooleanField()

    def __str__(self):
        return self.Name


