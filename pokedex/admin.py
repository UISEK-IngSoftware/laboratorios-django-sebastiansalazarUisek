from django.contrib import admin
from .models import Pokemon, Trainer  #Importar el modelo Pokémon para registrarlo en el panel de administración de Django

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    pass