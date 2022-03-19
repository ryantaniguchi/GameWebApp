from django.urls import path
from . import views

urlpatterns = [
    # Default page will pull from the views.home
    path('', views.home, name='home'),
    path('links/', views.links, name='links'),
    # Directs to a page to create new games in the database
    path('add-game/', views.add_game, name='add_game'),
    # Directs to a page for each game based on the BGGId
    path('game/<int:BGGId>', views.game_index, name='game_index'),

    # URL patterns related to index pages
    # Directs to the rated-index page
    path('rated-index/', views.rated_index, name='rated_index'),
    # Default page will pull from the views.home
    path('strategic-index/', views.strategic_index, name='strategic_index'),
    # Default page will pull from the views.home
    path('thematic-index/', views.thematic_index, name='thematic_index'),
    # Directs to a page with links to other websites
    path('war-index/', views.war_index, name='war_index'),
    # Directs to a page with links to other websites
    path('family-index/', views.family_index, name='family_index'),
    # Directs to a page with links to other websites
    path('cgs-index/', views.cgs_index, name='cgs_index'),
    # Directs to a page with links to other websites
    path('abstract-index/', views.abstract_index, name='abstract_index'),
    # Directs to a page with links to other websites
    path('party-index/', views.party_index, name='party_index'),
    # Directs to a page with links to other websites
    path('children-index/', views.children_index, name='children_index'),
    # Directs to a page with links to other websites
]