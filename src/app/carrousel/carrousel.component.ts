import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-carrousel',
  templateUrl: './carrousel.component.html',
  styleUrls: ['./carrousel.component.css']
})
export class CarrouselComponent implements OnInit {

  images = ['assets/img/planta/camarones.jpeg',
  'assets/img/planta/maquina.jpeg',
  'assets/img/planta/contenedor.jpeg'];

  noticia1:any={
    "img":"assets/img/planta/camarones.jpeg",
    "title":"Titulo prueba 1",
    "desc":"Aqui va la descripcion de la noticia"
  }
  noticia2:any={
    "img":"assets/img/planta/maquina.jpeg",
    "title":"Titulo prueba 2",
    "desc":"Aqui va la descripcion de la noticia"
  }
  noticia3:any={
    "img":"assets/img/planta/contenedor.jpeg",
    "title":"Titulo prueba 3",
    "desc":"Aqui va la descripcion de la noticia"
  }

  constructor(public _http: HttpClient) { }

  ngOnInit(): void {
    this.getUltimasNoticias(this._http);
  } 
  noticiasActuales: any;
  ultimos= [];
  getUltimasNoticias(_http:HttpClient){
    this._http.get('http://127.0.0.1:8000/getUltimasNoticias/')
    .subscribe(
      (data)=>{console.log(data);
        this.noticiasActuales=data;
        for (let key in this.noticiasActuales) {
          let notica = this.noticiasActuales[key];
          console.log(notica);
          this.ultimos.push(notica);
      }   
      }
      ,(err: HttpErrorResponse)=>{console.log("Un error ha ocurrido")}
      ,()=>console.log("solicitud finalizada OK")
      )
  }

}
