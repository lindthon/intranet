import { Component, OnInit } from '@angular/core';

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

  constructor() { }

  ngOnInit(): void {
  }

}
