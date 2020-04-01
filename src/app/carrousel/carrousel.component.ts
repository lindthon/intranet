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

  constructor() { }

  ngOnInit(): void {
  } 

}
