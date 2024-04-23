from django.urls import path

from .views import (
    list_of_coaches,
    coach_detail,
    list_of_leagues,
    league_detail,
    list_of_teams,
    team_detail,
    list_of_players,
    player_detail,
    team_player_list,
    league_team_list,
    coach_team
)

urlpatterns = [
    path('coaches/', list_of_coaches),
    path('coaches/<int:id>/', coach_detail),
    path('leagues/', list_of_leagues),
    path('leagues/<int:id>/', league_detail),
    path('teams/', list_of_teams),
    path('teams/<int:id>/', team_detail),
    path('players/', list_of_players),
    path('players/<int:id>/', player_detail),
    path('teams/<int:id>/players/', team_player_list),
    path('leagues/<int:id>/teams/', league_team_list),
    path('coaches/<int:id>/teams/', coach_team)
]