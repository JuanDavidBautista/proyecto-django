# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render,redirect
from .forms import VehiculosForm
from .models import Vehiculos
from django.contrib import messages


# Create your views here.
#===========================================================
#===========================================================
#===========================================================
#===========================================================
# ADMINISTRADOR ==================================

def RegistroVeh(request): 
    registroveh=VehiculosForm()
    return render(request,'registrarVeh.html',{'form':registroveh})
#---------------------------------------------------------------------




def GuardarVeh(request):
    if request.method == 'POST':
        registroveh = VehiculosForm(request.POST)
        if registroveh.is_valid():
            registroveh.save()
            return redirect('Vehiculo:listarvehiculo')
    
    return render(request, 'registrarVeh.html', {'form': VehiculosForm(), 'mensaje': 'vehiculo registrado'})




#===========================================================
def ListarVehiculos(request):
    listadoVehiculos=Vehiculos.objects.all()
    return render ( request,'listarVeh.html',{'listadoVehiculos':listadoVehiculos})



#===========================================================


def EditarVeh(request, id_veh):
    vehiculos=Vehiculos.objects.get(id_veh=id_veh)
    
    if request.method == 'POST':
        editavehiculos = VehiculosForm(data=request.POST, instance=vehiculos)
        if editavehiculos.is_valid():
            editavehiculos.save()
            return redirect('Vehiculo:listarvehiculo')
        else:
            return redirect('Vehiculo:editarvehiculo')

    registroveh = VehiculosForm(instance=vehiculos)
    return render(request, 'actualizarVeh.html', {'form': registroveh})

#===========================================================


def EliminarVeh(request,id_veh):
    vehiculodelete=Vehiculos.objects.get(id_veh=id_veh)
    vehiculodelete.delete()   
    return render(request,'listarVeh.html')























#===========================================================
#===========================================================
#===========================================================
#===========================================================
# TRABAJADOR ===============================================

def RegistroVehiculoEmp(request): 
    registrovehemp=VehiculosForm()
    return render(request,'registrarVehEmp.html',{'form':registrovehemp})

def GuardarVehiculoEmp(request):
    if request.method == 'POST':
        registroveh = VehiculosForm(request.POST)
        if registroveh.is_valid():
            # Guardar el diagnóstico en la base de datos
            vehiculo_text = registroveh.cleaned_data['vehiculo']
            vehiculo = Vehiculos(vehiculo=vehiculo_text)
            vehiculo.save()
            return render(request,'registrarVehEmp.html',{'form':registroveh,"mensaje":'vehiculo registrado correctamente'},)

#===========================================================


#===========================================================
def ListarVehiculosEmp(request):
    listadoVehiculosEmp=Vehiculos.objects.all()
    return render ( request,'listarVehEmp.html',{'listadoVehiculosEmp':listadoVehiculosEmp})




#===========================================================


def EditarVehiculosEmp(request, id_val):
    vehiculosEmp=Vehiculos.objects.get(id_val=id_val)
    
    if request.method == 'POST':
        editavehiculoemp = VehiculosForm(data=request.POST, instance=vehiculosEmp)
        if editavehiculoemp.is_valid():
            editavehiculoemp.save()
            return redirect('Vehiculo:listarvaloracionemplo')
        else:
            return redirect('Vehiculo:editarvehiculoemp')

    registrovehemp = VehiculosForm(instance=vehiculosEmp)
    return render(request, 'actualizarVehEmp.html', {'form': registrovehemp})

#===========================================================



def EliminarVehEmp(request,id_veh):
    vehiculodeleteemp=Vehiculos.objects.get(id_veh=id_veh)
    vehiculodeleteemp.delete()
    return render(request,'listarVehEmp.html')
