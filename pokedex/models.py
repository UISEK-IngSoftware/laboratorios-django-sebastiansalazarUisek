from django.db import models

# Create your models here.
class Trainer(models.Model):  #Definir el modelo de datos para un entrenador en la base de datos
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField()
    level = models.IntegerField (default=1)
    
    def __str__(self): #Definir cómo se representará un objeto Pokémon como una cadena de texto, en este caso, se mostrará su nombre
        return f"{self.first_name} {self.last_name}"

class Pokemon(models.Model):   #Definir el modelo de datos para un Pokémon en la base de datos
    name = models.CharField(max_length=100) 
    POKEMON_TYPES = {
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('P', 'Planta'),
        ('T', 'Tierra'),
        ('E', 'Electrico'),
        ('L', 'Lagartija'),
    }
    type = models.CharField(max_length=50, choices=POKEMON_TYPES, null=False)
    height = models.DecimalField(decimal_places=4, max_digits=6)
    weight = models.DecimalField(decimal_places=2, max_digits=6)
    trainer = models.ForeignKey(Trainer, on_delete = models.SET_NULL, null = True) #Definir una relación de clave foránea con el modelo Trainer, lo que significa que cada Pokémon puede estar asociado a un entrenador específico. Si el entrenador es eliminado, el campo se establecerá en NULL.
    picture = models.ImageField(upload_to="pokemon_images")

    def __str__(self): #Definir cómo se representará un objeto Pokémon como una cadena de texto, en este caso, se mostrará su nombre
        return self.name 