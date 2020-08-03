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


$('#buzon').dataTable( {
    "order": [[ 0, 'desc' ], [ 1, 'desc' ]]
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
