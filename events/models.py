from django.db import models
from entities.models import Hero, Villian


class Epic(models.Model):
    name = models.CharField(max_length=255)
    participating_heros = models.ManyToManyField(Hero)
    participating_villains = models.ManyToManyField(Villian)


class Event(models.Model):
    epic = models.ForeignKey(Epic, on_delete=models.CASCADE)
    datails = models.TextField()
    years_ago = models.PositiveIntegerField()


class EventHero(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    is_primary = models.BooleanField()


class EventVillian(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    hero = models.ForeignKey(Villian, on_delete=models.CASCADE)
    is_primary = models.BooleanField()
