import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-reglamento',
  templateUrl: './reglamento.component.html',
  styleUrls: ['./reglamento.component.css']
})
export class ReglamentoComponent implements OnInit {

  politicas:boolean=false;
  procedimientos:boolean=false;
  organigrama:boolean=false;

  constructor() { }

  ngOnInit(): void {
    this.politicas=true;
  }  

  showOrganigrama(){
    this.politicas=false;
    this.procedimientos=false;
    this.organigrama=true;    

  }

  showPoliticas(){    
    this.procedimientos=false;
    this.organigrama=false;
    this.politicas=true;
  }

  showProcedimientos(){
    this.politicas=false;    
    this.organigrama=false;
    this.procedimientos=true;
  }

}
