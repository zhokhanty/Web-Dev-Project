from rest_framework import serializers
from .models import Player, Coach, Team, League

class CoachSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField()
    country = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Coach.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance
    
    def delete(self, validated_data):
        return Coach.objects.delete(**validated_data)

class LeagueSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=100)
    image_url = serializers.CharField(max_length=255, allow_blank=True, required=False)

    def create(self, validated_data):
        return League.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.save()
        return instance
    
    def delete(self, validated_data):
        return Coach.objects.delete(**validated_data)

class TeamSerializer(serializers.ModelSerializer):
    league = serializers.PrimaryKeyRelatedField(queryset=League.objects.all())
    coach = serializers.PrimaryKeyRelatedField(queryset=Coach.objects.all())
    class Meta:
        model = Team
        fields = ['id', 'name', 'year', 'coach', 'league']

class PlayerSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    class Meta:
        model = Player
        fields = ['id', 'first_name', 'last_name', 'cost', 'age', 'country', 'position', 'team']