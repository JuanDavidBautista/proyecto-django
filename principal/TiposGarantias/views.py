from django.http import HttpRequest
from django.shortcuts import render,redirect
from .forms import TiposGarantiaForm
from .models import TiposGarantia
from django.contrib import messages
# Create your views here.

#===========================================================
#===========================================================
#===========================================================
#===========================================================
# ADMINISTRADOR ==================================
   
    
def Registro_Tipo_Garantia(request): 
    RegiTipoGarantia=TiposGarantiaForm()
    return render(request,'registro_tiga.html',{'form':RegiTipoGarantia})
  

#---------------------------------------------------------------------




def Guardar_Tipo_Garantia(request):
    if request.method == 'POST':
        RegiTipoGarantia = TiposGarantiaForm(request.POST)
        if RegiTipoGarantia.is_valid():
            # Guardar el diagnóstico en la base de datos
            nombre_text = RegiTipoGarantia.cleaned_data['nombre']
            tipgarantia = TiposGarantia(nombre=nombre_text)
            tipgarantia.save()
    return render(request,'registro_tiga.html',{'form':RegiTipoGarantia,"mensaje":'tipo de garantia -registrada'},)




 
#===========================================================  



def ListarTiposGarantia(request):
    listadoTipoGarantia=TiposGarantia.objects.all()
    return render ( request,'listar_tiga.html',{'listadoTipoGarantia':listadoTipoGarantia})



#===========================================================


def editar_TiposGarantia(request, id_tiga):
    tiposgarantias=TiposGarantia.objects.get(id_tiga=id_tiga)
    
    if request.method == 'POST':
        editatigarantia = TiposGarantiaForm(data=request.POST, instance=tiposgarantias)
        if editatigarantia.is_valid():
            editatigarantia.save()
            return redirect('TiposGarantias:listartiga')
        else:
            return redirect('TiposGarantias:editartiga')

    registrotiga = TiposGarantiaForm(instance=tiposgarantias)
    return render(request, 'editar_tiga.html', {'form': registrotiga})

#===========================================================


def eliminar_tiga(request,id_tiga):
    tigadelete=TiposGarantia.objects.get(id_tiga=id_tiga)
    tigadelete.delete()   
    return render(request,'listar_tiga.html')


