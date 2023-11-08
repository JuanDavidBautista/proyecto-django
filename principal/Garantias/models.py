
from django.db import models
# from Vehiculo.models import Serviciosxvehiculos
from TiposGarantias.models import TiposGarantia

class Garantias(models.Model):
    id_gar = models.AutoField(primary_key=True)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    id_tiga = models.ForeignKey(TiposGarantia, on_delete=models.CASCADE)
    def __str__(self):
        return f"Garantia {self.id_gar}"