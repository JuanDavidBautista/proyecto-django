from django.db import models

# Create your models here.

  
class TiposGarantia(models.Model):
    id_tiga = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

#----------------------------------------------------------------------------------------
