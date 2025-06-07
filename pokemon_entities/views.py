import folium

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime


from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, pokemon=None, request=None, image_url=None):
    if image_url is None:
        if pokemon and pokemon.image and request:
            image_url = request.build_absolute_uri(pokemon.image.url)
        else:
            image_url = DEFAULT_IMAGE_URL

    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    current_time = localtime()
    pokemons = Pokemon.objects.all()
    pokemon_entities = PokemonEntity.objects.select_related('pokemon').filter(
        appeared_at__lte=current_time,
        disappeared_at__gte=current_time
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            pokemon=pokemon_entity.pokemon,
            request=request
        )

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(
        Pokemon.objects.select_related('previous_evolution').prefetch_related('next_evolutions'),
        id=pokemon_id
    )
    pokemon_entities = pokemon.entities.all().select_related('pokemon')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            pokemon=pokemon_entity.pokemon,
            request=request
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemon,
        'DEFAULT_IMAGE_URL': DEFAULT_IMAGE_URL,
    })

