import { Component, OnInit } from '@angular/core';

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

  constructor() { }

  ngOnInit(): void {
  } 

}
