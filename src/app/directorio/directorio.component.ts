import { Component,HostListener,ViewChild, OnInit } from '@angular/core';
import { HttpClient, HttpResponse, HttpErrorResponse } from '@angular/common/http';
import {  LocalDataSource } from 'ng2-smart-table';

@Component({
  selector: 'app-directorio',
  templateUrl: './directorio.component.html',
  styleUrls: ['./directorio.component.css']
})
export class DirectorioComponent implements OnInit {

  empleados: any;
  data2=[];


  source: LocalDataSource ;
  constructor(public  _http: HttpClient) { 
    this.getEmpleados(_http);


  }

 
   settings = {
    actions: {
      delete: false,
      add: false,
      edit:false,      
    },
    columns: {
      
      Nombre: {
        title: 'Full Name',
      },      
      Correo: {
        title: 'Email',
      },
      Ubicacion: {
        title: 'Oficina',
      },
      Extension: {
        title: 'Exten sion',
      }
    },
  };
  datas = [
    {
      id: 1,
      name: "Leanne Graham",      
      email: "Sincere@april.biz",
      office:"Planta 1",
      ext:"256"
    },
    {
      id: 2,
      name: "Ervin Howell",
      username: "Antonette",
      email: "Shanna@melissa.tv",
      office:"Planta 1",
      ext:"255"
    },
    {
      id: 1,
      name: "Leanne Graham",
      username: "Bret",
      email: "Sincere@april.biz",
      office:"Planta 2",
      ext:"128"
    },
    {
      id: 2,
      name: "Ervin Howell",
      username: "Antonette",
      email: "Shanna@melissa.tv",
      office:"Oficina Centro",
      ext:"222"
    },
    {
      id: 1,
      name: "Leanne Graham",
      username: "Bret",
      email: "Sincere@april.biz",
      office:"Planta 1",
      ext:"222"
    },
    {
      id: 2,
      name: "Ervin Howell",
      username: "Antonette",
      email: "Shanna@melissa.tv",
      office:"Planta 1",
      ext:"222"
    },
    {
      id: 1,
      name: "Leanne Graham",
      username: "Bret",
      email: "Sincere@april.biz",
      office:"Planta 2",
      ext:"222"
    },
    {
      id: 2,
      name: "Ervin Howell",
      username: "Antonette",
      email: "Shanna@melissa.tv",
      office:"Planta 2",
      ext:"222"
    },
    {
      id: 1,
      name: "Leanne Graham",
      username: "Bret",
      email: "Sincere@april.biz",
      office:"Oficina Centro",
      ext:"222"
    },
    {
      id: 2,
      name: "Ervin Howell",
      username: "Antonette",
      email: "Shanna@melissa.tv",
      office:"Oficina Centro",
      ext:"222"
    },

    // ... list of items
  ];

  ngAfterViewInit() {
    console.log("afterinit");
    setTimeout(() => {
      

    }, 1000);
    
  }


   //Metodo para obtener empleados
  getEmpleados(_http: HttpClient){
    this._http.get('http://127.0.0.1:8000/getContacto/')
      .subscribe(
        (data)=>{console.log(data);
          this.empleados=data;
          for (let key in this.empleados) {
            let empleado = this.empleados[key];
            this.data2.push(empleado);
            this.source = new LocalDataSource(this.data2);
        }   
        }
        ,(err: HttpErrorResponse)=>{console.log("Un error ha ocurrido")}
        ,()=>console.log("solicitud finalizada OK")
        )
  }

  onDeleteConfirm(event) {
    console.log("Delete Event In Console")
    console.log(event);
    if (window.confirm('Are you sure you want to delete?')) {
      event.confirm.resolve();
    } else {
      event.confirm.reject();
    }
  }

  onCreateConfirm(event) {
    console.log("Create Event In Console")
    console.log(event);

  }

  onSaveConfirm(event) {
    console.log("Edit Event In Console")
    console.log(event);
  }
  
  ngOnInit(): void {

  }
}
