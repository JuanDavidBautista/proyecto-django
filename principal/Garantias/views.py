from django.shortcuts import render,redirect
from .forms import GarantiasForm
from .models import Garantias
# Create your views here.



#=======================================================
#=======================================================
#=======================================================
#=================_GARANTIAS============================





def Listar_Garantia(request):
    listadoGarantias=Garantias.objects.all()
    return render(request,'listar_garantias.html',{'listadoGarantias':listadoGarantias})

#---------------------------------------------------------------------


def Registro_Garantia(request):
    RegiGarantia=GarantiasForm()
    return render(request,'registrar_garantias.html',{'form':RegiGarantia})

#---------------------------------------------------------------------

def Guardar_Garantia(request):
    if request.method == 'POST':
        RegiGarantia = GarantiasForm(request.POST)
        if RegiGarantia.is_valid():
            RegiGarantia.save()
            return redirect('Garantias:listargarantia')
    
    return render(request, 'registrar_garantias.html', {'form': GarantiasForm(), 'mensaje': 'Tipo de garantía registrada'})





#---------------------------------------------------------------------
def Editar_Garantia(request, id_gar):
    garantia = Garantias.objects.get(id_gar=id_gar)
    
    if request.method == 'POST':
        form = GarantiasForm(request.POST, instance=garantia)
        if form.is_valid():
            form.save()
            return redirect('Garantias:listargarantia')
    
    return render(request, 'editar_garantias.html', {'form': GarantiasForm(instance=garantia)})

#---------------------------------------------------------------------



def eliminar_garantia(request,id_gar):
    garantiadelete=Garantias.objects.get(id_gar=id_gar)
    garantiadelete.delete()   
    return render(request,'listar_garantias.html')



#---------------------------------------------------------------------
