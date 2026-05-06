from django.db import models

# Create your models here.
class Pokemon(models.Model):   #Definir el modelo de datos para un Pokémon en la base de datos
    name = models.CharField(max_length=100) 
    type = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    
    def __str__(self): #Definir cómo se representará un objeto Pokémon como una cadena de texto, en este caso, se mostrará su nombre
        return self.name 