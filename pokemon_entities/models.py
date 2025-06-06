from django.db import models



class Pokemon(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name="Название")
    title_en = models.CharField(max_length=200, blank=True, verbose_name="Название (англ)")
    title_jp = models.CharField(max_length=200, blank=True, verbose_name="Название (япон)")
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name="Изображение")
    description = models.TextField(blank=True, verbose_name="Описание")

    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='next_evolutions',
        verbose_name="Предыдущая эволюция"
    )


def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField(verbose_name='Lat')
    longitude = models.FloatField(verbose_name='Lon')
    appeared_at = models.DateTimeField(verbose_name='Appeared at', null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name='Disappeared at', null=True, blank=True)

    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defense = models.IntegerField()
    stamina = models.IntegerField()

    def __str__(self):
        return f'{self.pokemon.title} ({self.latitude}, {self.longitude})'
