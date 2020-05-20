import { Component,ViewChild,ElementRef, OnInit } from '@angular/core';

@Component({
  selector: 'app-sugerencias',
  templateUrl: './sugerencias.component.html',
  styleUrls: ['./sugerencias.component.css']
})

export class SugerenciasComponent implements OnInit {

  constructor() { }
   @ViewChild("sugerencia") sugerencia :ElementRef ;

    
    email: string;
    suggestion: string;
    selectedLink: string;        
    option: string;
  
 
  @ViewChild('form') formGroup;
    ngOnInit():void {
       
        console.log(this.formGroup); // Inspect the object for other available property and methods.
    }

  ngAfterViewInit() {
    console.log("afterinit");
    setTimeout(() => {
      
      console.log(this.sugerencia.nativeElement.innerHTML);

    }, 1000);
    
  }
    setOption(e: string): void   {  
        this.selectedLink = e;    
    }  
    
    isSelected(name: string): string   {  
        if (!this.selectedLink) { 
            return "No seleccionado";  

        }if(this.selectedLink==="option6"){
            return this.option = this.formGroup.nativeElement[6].value;
        }  
        return name;  
    }  

  //Action Button
   sendData() {
    
     console.log(this.sugerencia.nativeElement.innerHTML);
     console.log(this.formGroup); 

     this.suggestion = this.formGroup.nativeElement[7].value;
     this.email = this.formGroup.nativeElement[8].value;
     this.option = this.isSelected(this.selectedLink);

     console.log("Variable "+ this.option);
     console.log("Variable "+ this.suggestion);
     console.log("Variable "+ this.email);

     //Limpio variables
     this.suggestion = "";
     this.email = "";
     this.option = "";
 }

  
    
  
}
