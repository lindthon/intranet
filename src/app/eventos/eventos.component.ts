import { Component, OnInit } from '@angular/core';
import { faClock,faMapMarkerAlt } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-eventos',
  templateUrl: './eventos.component.html',
  styleUrls: ['./eventos.component.css']
})
export class EventosComponent implements OnInit {

  faClock=faClock;
  faMapMarkerAlt=faMapMarkerAlt;
  
  events:any=[{
    "day":"3",
    "month":"Marzo",
    "year":"2020",
    "time":"ALL DAY",
    "title":"Inauguracion",
    "desc":"Inauguracion de algún evento de santa priscila",
    "place":"Planta 1"
  },
  {
    "day":"5",
    "month":"Septiembre",
    "year":"2020",
    "time":"ALL DAY",
    "title":"Inauguracion 2",
    "desc":"Inauguracion de algún evento de santa priscila",
    "place":"Planta 2"
  }
]
  constructor() { }
  p:number =1;
  ngOnInit(): void {
  }

}
