import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-brigadas',
  templateUrl: './brigadas.component.html',
  styleUrls: ['./brigadas.component.css']
})
export class BrigadasComponent implements OnInit {
  colaborativo:any={
    "img":"assets/img/team/team02.jpg",
    "name":"Jaime Alarcón",
    "label":"Empleado más colaborativo"
  };
  colaborativo2:any={
    "img":"assets/img/team/team03.jpg",
    "name":"Jaime Alarcón",
    "label":"Empleado más colaborativo"
  };
  colaborativo3:any={
    "img":"assets/img/team/team04.jpg",
    "name":"Jaime Alarcón",
    "label":"Empleado más colaborativo"
  };
  constructor(public _http:HttpClient) { 
    this.getNoticiasPorCategoria(_http);
  }

  ngOnInit(): void {
    console.log(this.nombresBrigadas);
    console.log("val")
    console.log(this.diccionarioBrigadas);
  }

   NoticiasPorCategoria: any;
  arrayCategoria =[];
  NewsCater:any;/*Variable que para la noticias */
  arrayNoticiasCate= [];
  arrayNoticiasCate2 = [];

  note : any;
  contador_noticias: number=0;



  brigadas:any;
  nombresBrigadas=[];
  diccionarioBrigadas=[];
  getNoticiasPorCategoria(_http:HttpClient){
    this._http.get('http://127.0.0.1:8000/get_brigada/')
    .subscribe(
      (data)=>{console.log(data);
        this.NoticiasPorCategoria=data;
        this.diccionarioBrigadas.push(data);
        for (let keyCategoria in data) {
          console.log(keyCategoria)
          this.nombresBrigadas.push(keyCategoria);
          let NewsCater = data[keyCategoria];
          console.log("categoria")
          console.log(NewsCater);
          this.note- NewsCater;
          this.contador_noticias=this.contador_noticias+1;
          this.arrayCategoria.push(keyCategoria)
          for(let keyNoticia in NewsCater){
            let noticia = NewsCater[keyNoticia];
            console.log("noticia")
            this.arrayNoticiasCate.push(noticia)
            console.log(noticia);
         }
        }
        ;console.log(this.contador_noticias);
      }
      ,(err: HttpErrorResponse)=>{console.log("Un error ha ocurrido")}
      ,()=>console.log("solicitud finalizada OK")
      )
  }


}
