from django.urls import path
from Login.views import proteccion_rutas

from . import views

app_name = 'Vehiculo'



urlpatterns = [
    
    path('login/admin/registrarvehiculo/', proteccion_rutas([1])(views.RegistroVeh), name='registrarvehiculo'),
    path('login/admin/guardarvehiculo/', proteccion_rutas([1])(views.GuardarVeh), name='guardarvehiculo'),
    path('login/admin/listarvehiculo/',proteccion_rutas([1])(views.ListarVehiculos),name='listarvehiculo') ,
    path('login/admin/editarvehiculo/<id_veh>/',proteccion_rutas([1])(views.EditarVeh),name='editarvehiculo') ,
    path('login/admin/listarvehiculo/eliminarvehiculo/<id_veh>/',proteccion_rutas([1])(views.EliminarVeh),name='eliminarvehiculo') ,


    # path('HomeLoc/admin/registrarVehEmp/', proteccion_rutas([2])(views.RegistroVehiculoEmp), name='registrarvehiculoemp'),
    # path('HomeLoc/admin/guardarVehEmp/', proteccion_rutas([2])(views.GuardarVehiculoEmp), name='guardarvehiculoemp'),
    # path('HomeLoc/admin/listarvVehEmp/',proteccion_rutas([2])(views.ListarVehiculosEmp),name='listarvehiculoemp') ,
    # path('HomeLoc/admin/editarVehEmp/<id_veh>/',proteccion_rutas([2])(views.EditarVehiculosEmp),name='editarvehiculoemp') ,
    # path('HomeLoc/admin/listarVehEmp/eliminarVeh/<id_veh>/',proteccion_rutas([2])(views.EliminarVehEmp),name='eliminarvehiculoemp') ,

    
]