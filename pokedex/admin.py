from django.contrib import admin
from .models import Pokemon  #Importar el modelo Pokémon para registrarlo en el panel de administración de Django

admin.site.register(Pokemon) #Registrar el modelo Pokémon para que sea accesible y gestionable a través del panel de administración de Django
