from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    descrip = models.TextField(blank=True) # si no pasa nada por defecto estara en blanco
    created = models.DateTimeField(auto_now_add=True) # va añadir la fecha 
    datecompleted = models.DateTimeField(null=True, blank=True) # fecha de cuando se completo
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Para que se relacione con la tabla de usuarios por una key (ID)

    def __str__(self):
        return self.title + ' - By ' + self.user.username