from django.urls import path
from . import views

urlpatterns = [   
   #INDEX DE LA PAGINA 
   path('',views.index,name='index'),
   
]