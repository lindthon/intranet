
async function getEmpleados(id) {
    let response = await fetch('http://127.0.0.1:8000/getEmpleadoPorCedula/'+id);
    console.log(response.status); // 200
    console.log(response.statusText); // OK
    if (response.status === 200) {
        let data = await response.json();
        console.log(data);
        document.getElementById("name").value = data["Nombre"];
        document.getElementById("apellido").value = data["Apellido"];
        document.getElementById("correo").value = data["Correo"];
        document.getElementById("cedula").value = data["Cedula"];
        document.getElementById("fecha").value = data["Fecha"];
        document.getElementById("usuario").value = data["User"];
        document.getElementById("extension").value = data["Extension"];
        document.getElementById("id_empleado").value = id;

        var val = window.location.href+id;
        console.log(val);
        // handle data
    }
}

function confirmationMessage(id){
    var value = confirm("Seguro que deseas eliminar este elemento ?");
    if(value && id){
       document.forms['myform'+id].submit();
       window.close();
    }
}

async function postEmpleados(){
    var id = document.getElementById("id_empleado").value;
    console.log(id)
    fetch('http://127.0.0.1:8000/modificarEmpleado/'+'0958561029', { 
    // Adding method type 
    method: "POST", 
    // Adding body or contents to send 
    body: JSON.stringify({ 
        name: document.getElementById("name").value, 
        apellido:document.getElementById("apellido").value , 
    }),   
    }) 
        // Converting to JSON 
        .then(response => response.json()) 
        
        // Displaying results to console 
        .then(json => console.log(json)); 


}

$(document).ready(function() {
    $('#dataTable').DataTable( {
        "language": {
            "lengthMenu": "Mostrar _MENU_ entradas",
            "zeroRecords": "No se ha encontrado nada - :c",
            "info": "Mostrar página _PAGE_ de _PAGES_",
            "infoEmpty": "No encontrado",
            "infoFiltered": "(filtrado de _MAX_ en total)",
            "search": "Buscar:",
            "paginate": {
                "previous":   "Anterior",
                "next":       "Siguiente",
            },

        }
    } );
} );


$(document).ready(function() {
    $('#buzonTable').DataTable( {
        "language": {
            "lengthMenu": "Mostrar _MENU_ entradas",
            "zeroRecords": "No se ha encontrado nada - :c",
            "info": "Mostrar página _PAGE_ de _PAGES_",
            "infoEmpty": "No encontrado",
            "infoFiltered": "(filtrado de _MAX_ en total)",
            "search": "Buscar:",
            "paginate": {
                "previous":   "Anterior",
                "next":       "Siguiente",
            },
        }
    } );
} );

