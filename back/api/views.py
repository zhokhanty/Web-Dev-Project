from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Coach, League, Team, Player
from .serializers import CoachSerializer, LeagueSerializer, TeamSerializer, PlayerSerializer

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Coach, League, Team, Player
from .serializers import CoachSerializer, LeagueSerializer, TeamSerializer, PlayerSerializer

@api_view(['GET', 'POST'])
def list_of_coaches(request):
    if request.method == 'GET':
        coaches = Coach.objects.all()
        serializer = CoachSerializer(coaches, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = CoachSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def coach_detail(request, id):
    try:
        coach = Coach.objects.get(id=id)
    except Coach.DoesNotExist:
        return JsonResponse({"Coach Not Found": "This coach does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CoachSerializer(coach)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = CoachSerializer(coach, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        coach.delete()
        return JsonResponse({"This coach is deleted": True})
    
@api_view(['GET', 'POST'])
def list_of_leagues(request):
    if request.method == 'GET':
        leagues = League.objects.all()
        serializer = LeagueSerializer(leagues, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = LeagueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def league_detail(request, id):
    try:
        league = League.objects.get(id=id)
    except League.DoesNotExist:
        return JsonResponse({"League Not Found": "This league does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LeagueSerializer(league)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = LeagueSerializer(league, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        league.delete()
        return JsonResponse({"This league is deleted": True})
    
@api_view(['GET', 'POST'])
def list_of_teams(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, id):
    try:
        team = Team.objects.get(id=id)
    except Team.DoesNotExist:
        return JsonResponse({"Team Not Found": "This team does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TeamSerializer(team)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = TeamSerializer(team, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        team.delete()
        return JsonResponse({"This team is deleted": True})
    
@api_view(['GET', 'POST'])
def list_of_players(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def player_detail(request, id):
    try:
        player = Player.objects.get(id=id)
    except Player.DoesNotExist:
        return JsonResponse({"Player Not Found": "This player does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PlayerSerializer(player)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = PlayerSerializer(player, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        player.delete()
        return JsonResponse({"This player is deleted": True})