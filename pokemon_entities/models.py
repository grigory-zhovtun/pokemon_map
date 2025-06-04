from django.db import models



class Pokemon(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField(verbose_name='Lat')
    longitude = models.FloatField(verbose_name='Lon')
    appeared_at = models.DateTimeField(verbose_name='Appeared at', null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name='Disappeared at', null=True, blank=True)

    def __str__(self):
        return f'{self.pokemon.title} ({self.latitude}, {self.longitude})'
