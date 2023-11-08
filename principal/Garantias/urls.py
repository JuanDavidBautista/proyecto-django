
from django.urls import path 
from Login.views import proteccion_rutas
from .import views

app_name = 'Garantias'

urlpatterns = [

path('login/admin/listargarantia/', proteccion_rutas([1])(views.Listar_Garantia), name='listargarantia'),
 path('login/admin/registrogarantia/', proteccion_rutas([1])(views.Registro_Garantia), name='registrogarantia'),
 path('login/admin/guardargarantia/', proteccion_rutas([1])(views.Guardar_Garantia), name='guardargarantia'),
 path('login/admin/editargarantia/<id_gar>/',proteccion_rutas([1])(views.Editar_Garantia),name='editargarantia') ,
path('login/admin/listargarantia/eliminargarantia/<id_gar>/',proteccion_rutas([1])(views.eliminar_garantia),name='eliminargarantia') ,
 
 

]
 