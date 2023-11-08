from django.urls import path
from Login.views import proteccion_rutas

from . import views

app_name = 'TiposGarantias'



urlpatterns = [
    
    

    path('login/admin/registrartiga/', proteccion_rutas([1])(views.Registro_Tipo_Garantia), name='registrartiga'),
    path('login/admin/guardartiga/', proteccion_rutas([1])(views.Guardar_Tipo_Garantia), name='guardartiga'),
    path('login/admin/listartiga/',proteccion_rutas([1])(views.ListarTiposGarantia),name='listartiga') ,
    path('login/admin/editartiga/<id_tiga>/',proteccion_rutas([1])(views.editar_TiposGarantia),name='editartiga') ,
    path('login/admin/listartiga/eliminartiga/<id_tiga>/',proteccion_rutas([1])(views.eliminar_tiga),name='eliminartiga') ,


   

]


