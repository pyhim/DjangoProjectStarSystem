from django.db import models
from django.urls import reverse
from math import pi

# Create your models here.


class Galaxy(models.Model):
    name = models.CharField(max_length=100, default=None)
    size_x = models.PositiveIntegerField(default=None)
    size_y = models.PositiveIntegerField(default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('galaxy-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Galaxies'
        ordering = ['-id']


class StarSystem(models.Model):
    name = models.CharField(max_length=100, default=None)
    position_x = models.PositiveIntegerField(default=None)
    position_y = models.PositiveIntegerField(default=None)
    galaxy = models.ForeignKey(
        'StarSystem.Galaxy',
        on_delete=models.SET_NULL,
        null=True,
        related_name='starsystems'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('starsystem-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'StarSystems'
        ordering = ['galaxy']


class Star(models.Model):
    name = models.CharField(max_length=100, default=None)
    diameter = models.PositiveIntegerField(default=None)
    color = models.CharField(max_length=100, default=None)
    star_system = models.ForeignKey(
        'StarSystem.StarSystem',
        on_delete=models.SET_NULL,
        null=True,
        related_name='stars'
    )

    @property
    def square(self):
        s = (pi * self.diameter) ** 2
        return s

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('star-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Stars'
        ordering = ['star_system']


class Planet(models.Model):
    name = models.CharField(max_length=100, default=None)
    diameter = models.PositiveIntegerField(default=None)
    color = models.CharField(max_length=100, default=None)
    star_system = models.ForeignKey(
        'StarSystem.StarSystem',
        on_delete=models.SET_NULL,
        null=True,
        related_name='planets'
    )
    life = models.BooleanField(default=False)

    @property
    def square(self):
        s = (pi * self.diameter) ** 2
        return s

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('planet-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Planets'
        ordering = ['star_system']
