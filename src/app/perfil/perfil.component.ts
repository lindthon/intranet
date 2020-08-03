import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.css']
})
export class PerfilComponent implements OnInit {
  constructor(public _http:HttpClient) {
    console.log(localStorage.getItem("user"));
    this.getByUserName(_http);
   }

  ngOnInit(): void {
  }
  nombre: string;
  apellido:string;
  correo:string;
  image:string;

  usuarios = [];
  getByUserName(_http: HttpClient){
    this._http.get('http://127.0.0.1:8000/get_user/?id='+localStorage.getItem("user"))
    .subscribe(
      (data)=>{console.log(data);
        console.log(data['correo'])
        this.nombre=data['nombre']
        this.apellido=data['apellido']
        this.correo=data['correo']
        this.image=data['img']

      }
      ,(err: HttpErrorResponse)=>{console.log("Un error ha ocurrido")}
      ,()=>console.log("solicitud finalizada OK")
      )

  }

}
