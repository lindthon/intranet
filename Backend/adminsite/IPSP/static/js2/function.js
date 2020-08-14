var loadFile = function(event) {
    var output = document.getElementById('image_eslogan');
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function() {
      URL.revokeObjectURL(output.src) // free memory
    }
  };

  var loadFilePrincipal = function(event) {
    var output = document.getElementById('image_principal');
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function() {
      URL.revokeObjectURL(output.src) // free memory
    }


  };

  function myalert(){
            alert("Modificacion exitosa !!!");

        }