
//  funcion de js pára eliminar los TIPOS DE GARANTIAS 

function eliminar(id_tiga) {


 

    swal({
        title: "¡Eliminar un Registro!",
        text:       "¿Estas seguro?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
         window.location.href="eliminartiga/"+ id_tiga +"/";
        }

        if (willDelete) {
          window.location.href = '/login/admin/listartiga/';  
        } 


      });

    


}










//===================//============//=================
function eliminar_garantia(id_gar) {
  swal({
    title: "¡Eliminar un Registro!",
    text: "¿Estás seguro?",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      window.location.href = "eliminargarantia/" + id_gar + "/";
    }
    if (willDelete) {
      window.location.href = '/login/admin/listargarantia/';
    }
  });
}







//===================//============//=================
function eliminarvehiculo(id_veh) {
  swal({
    title: "¡Eliminar un Registro!",
    text: "¿Estás seguro?",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      window.location.href = "eliminarvehiculo/" + id_veh + "/";
    }
    if (willDelete) {
      window.location.href = '/login/admin/listarvehiculo/';
    }
  });
}

