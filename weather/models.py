from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):  # Show the actual city name on the dashboar
        return self.name

    class Meta:  # Show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'
