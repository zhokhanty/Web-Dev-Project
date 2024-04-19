from django.db import models

class Coach(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"first_name: {self.first_name}, last_name: {self.last_name}, date_of_birth: {self.date_of_birth}, country: {self.country}"
    
class League(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"name: {self.name}, country: {self.country}"

class Team(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name="coach")
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="league")

    def __str__(self):
        return f"name: {self.name}, year: {self.year}, coach: {self.coach.first_name and self.coach.last_name}, league: {self.league.name}"
    
class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cost = models.FloatField()
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team")

    def __str__(self):
        return f"first_name: {self.first_name}, last_name: {self.last_name}, cost: {self.cost}, age: {self.age}, country: {self.country}, position: {self.position}, team: {self.team.name}"