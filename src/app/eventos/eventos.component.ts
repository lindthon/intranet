import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-eventos',
  templateUrl: './eventos.component.html',
  styleUrls: ['./eventos.component.css']
})
export class EventosComponent implements OnInit {

  
  news:any=[{
    "image":"assets/img/planta/camarones.jpeg",
    "date":"MAY 8, 2018",
    "id":"1",
    "title":"Titulo de Camarones",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/maquina.jpeg",
    "date":"MAY 8, 2018",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/sistema.jpeg",
    "date":"MAY 8, 2018",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/contenedor.jpeg",
    "date":"MAY 8, 2018",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/camarones.jpeg",
    "date":"MAY 8, 2018",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/sistema.jpeg",
    "date":"MAY 8, 2018",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/maquina.jpeg",
    "date":"MAY 8, 2018",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/contenedor.jpeg",
    "date":"MAY 8, 2018",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/camarones.jpeg",
    "date":"MAY 8, 2018",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/contenedor.jpeg",
    "date":"MAY 8, 2018",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  }
]
  constructor() { }
  p:number =1;
  ngOnInit(): void {
  }

}
