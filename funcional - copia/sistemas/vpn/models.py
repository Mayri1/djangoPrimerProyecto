from django.db import models

# Create your models here.
class Usuario(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)

def __str__(self):
    fila = "Nombre: " + self.name + " - " + "Contraseña: " + self.contraseña
    return fila

""" def delete(self, using=None, keep_parents=False):
    self.imagen.delete(self.imagen.name)
    super().delete()  """
