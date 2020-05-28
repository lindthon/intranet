import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {

  asistencia:any={
    "img":"assets/img/team/team01.jpg",
    "name":"Ericka Valle",
    "label":"Asistencia perfecta"
  };
  colaborativo:any={
    "img":"assets/img/team/team02.jpg",
    "name":"Jaime Alarcón",
    "label":"Empleado más colaborativo"
  };
  agil:any={
    "img":"assets/img/team/team03.jpg",
    "name":"Luisa Camallo",
    "label":"Empleado más ágil"
  };

  constructor(public _http:HttpClient) {

   }

  ngOnInit(): void {
    this.getMejoresEmpleados(this._http)

  }
  datos : any;
  empleados = [];
  getMejoresEmpleados(_http:HttpClient){
    this._http.get('http://127.0.0.1:8000/getMejoresEmpleados/')
    .subscribe(
      (data)=>{console.log(data);
        this.datos=data;
        for (let key in this.datos) {
          let empleado = this.datos[key];
          console.log(empleado);
          this.empleados.push(empleado);
      }   
      }
      ,(err: HttpErrorResponse)=>{console.log("Un error ha ocurrido")}
      ,()=>console.log("solicitud finalizada OK")
      )
  }

}
