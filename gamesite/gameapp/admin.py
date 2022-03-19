from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here

# Grants the admin site access to Game
admin.site.register(Game)

class GameAdmin(ImportExportModelAdmin):
    list_display = ('BGGId', 'Name', 'AvgRating', 'NumRatings', 'Playtime', 'Thematic', 'Strategy', 'War', 'Family', 'CGS', 'Abstract', 'Party', 'Child')
