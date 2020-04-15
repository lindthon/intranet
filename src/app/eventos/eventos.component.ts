import { Component, OnInit, ViewChild } from '@angular/core';
import { faClock,faMapMarkerAlt } from '@fortawesome/free-solid-svg-icons';
import { IgxMonthPickerComponent } from "igniteui-angular";

@Component({
  selector: 'app-eventos',
  templateUrl: './eventos.component.html',
  styleUrls: ['./eventos.component.css']
})
export class EventosComponent implements OnInit {
  @ViewChild(IgxMonthPickerComponent, { static: true })
    public monthPicker;


  faClock=faClock;
  faMapMarkerAlt=faMapMarkerAlt;

  date: Date = new Date(Date.now());
  locale: "es";
  formatOptions = {
    month: "long",
    year: "numeric"
  };


  events:any;

  enero:any=[{
    "day":"1",
    "month":"Enero",
    "year":"2020",
    "time":"ALL DAY",
    "title":"Inauguracion",
    "desc":"Inauguracion de algún evento de santa priscila",
    "place":"Planta 1"
  },
  {
    "day":"13",
    "month":"Enero",
    "year":"2020",
    "time":"10:00",
    "title":"Inauguracion 2",
    "desc":"Inauguracion de algún evento de santa priscila",
    "place":"Planta 2"
  }
]

febrero:any=[{
  "day":"5",
  "month":"Febrero",
  "year":"2020",
  "time":"9:00",
  "title":"Inauguracion 2",
  "desc":"Inauguracion de algún evento de santa priscila",
  "place":"Planta 2"
}
]

marzo:any=[{
  "day":"3",
  "month":"Marzo",
  "year":"2020",
  "time":"16:00",
  "title":"Inauguracion",
  "desc":"Inauguracion de algún evento de santa priscila",
  "place":"Planta 1"
},
{
  "day":"5",
  "month":"Marzo",
  "year":"2020",
  "time":"ALL DAY",
  "title":"Inauguracion 2",
  "desc":"Inauguracion de algún evento de santa priscila",
  "place":"Planta 2"
},
{
  "day":"25",
  "month":"Marzo",
  "year":"2020",
  "time":"10:00",
  "title":"Inauguracion 3",
  "desc":"Inauguracion de algún evento de santa priscila",
  "place":"Planta 2"
}
]

abril:any=[{
  "day":"5",
  "month":"Abril",
  "year":"2020",
  "time":"13:30",
  "title":"Inauguracion 2",
  "desc":"Inauguracion de algún evento de santa priscila",
  "place":"Planta 2"
},
{
  "day":"10",
  "month":"Abril",
  "year":"2020",
  "time":"9:00",
  "title":"Inauguracion 3",
  "desc":"Inauguracion de algún evento de santa priscila",
  "place":"Planta 2"
},
{
  "day":"17",
  "month":"Abril",
  "year":"2020",
  "time":"ALL DAY",
  "title":"Inauguracion 4",
  "desc":"Inauguracion de algún evento de santa priscila",
  "place":"Planta 2"
},
{
  "day":"20",
  "month":"Abril",
  "year":"2020",
  "time":"20:00",
  "title":"Inauguracion 5",
  "desc":"Inauguracion de algún evento de santa priscila",
  "place":"Planta 2"
},
{
  "day":"30",
  "month":"Abril",
  "year":"2020",
  "time":"9:00",
  "title":"Inauguracion 6",
  "desc":"Inauguracion de algún evento de santa priscila",
  "place":"Planta 2"
}
]

  constructor() { }
  p:number =1;

  ngOnInit(): void {
    this.loadEvents();
    //this.events=this.enero;
  }

  loadEvents(){
    let month:String =this.monthPicker._viewDate.toString().substring(4,7);
    console.log(month);
    /*switch(month){
      case "Jan":{
        console.log(this.events);
        this.events=this.enero;
        console.log(this.events);
      }
      case "Feb":{
        this.events=this.febrero;  
      }
      case "Mar":{
        this.events=this.marzo;  
      }
      case "Apr":{
        this.events=this.abril;
      }
      default:
    }*/
    if(month=="Jan")
      this.events=this.enero;
    else if(month=="Feb")
      this.events=this.febrero;
    else if(month=="Mar")
      this.events=this.marzo;
    else if(month=="Apr")
      this.events=this.abril;
    else
      this.events=[];
    console.log(this.events);
  }
}
