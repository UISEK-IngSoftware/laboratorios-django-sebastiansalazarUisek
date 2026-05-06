from django.http import HttpResponse
from django.template import loader
from .models import Pokemon

def index(request):
    pokemons = Pokemon.objects.all()  #Obtener todos los objetos Pokémon de la base de datos utilizando el modelo Pokémon (Select * from pokedex_pokemon)
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, id: int):
    pokemon = Pokemon.objects.get(id=id) #Obtener un objeto Pokémon específico de la base
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))