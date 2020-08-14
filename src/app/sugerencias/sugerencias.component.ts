import { Component,ViewChild,ElementRef, OnInit } from '@angular/core';
import { HttpClient, HttpResponse, HttpErrorResponse } from '@angular/common/http';
import { FormGroup, FormGroupDirective } from '@angular/forms';

@Component({
  selector: 'app-sugerencias',
  templateUrl: './sugerencias.component.html',
  styleUrls: ['./sugerencias.component.css']
})

export class SugerenciasComponent implements OnInit {

   myForm: FormGroup;

  // @ViewChild("sugerencia") sugerencia :ElementRef ;

    
    email: string;
    suggestion: string;
    selectedLink: string;        
    option: string;

    data: any;
    tipo: any;
 
  @ViewChild('form') formGroup;
    ngOnInit():void {
       
        //console.log(this.formGroup); // Inspect the object for other available property and methods.
    }

  ngAfterViewInit() {
    console.log("afterinit");
    setTimeout(() => {
      
     // console.log(this.sugerencia.nativeElement.innerHTML);

    }, 1000);
    
  }
    setOption(e: string): void   {  
        this.selectedLink = e;    
    }  
    
    isSelected(name: string): string   {  
        if (!this.selectedLink) { 
            return "No seleccionado";  

        /* }if(this.selectedLink==="option6"){
          this.option = this.formGroup.nativeElement[6].value;
          this.tipo = {
                    "nuevaSugerencia": this.option,
                      }
        //  this.postNuevoTipoSugerencia(this._http);
            return this.option = this.formGroup.nativeElement[6].value;*/
        }  
        return name;  
    }  

  //Action Buttuon
   sendData() {
    
//     console.log(this.sugerencia.nativeElement.innerHTML);
  //   console.log(this.formGroup); 

    /* this.suggestion = this.formGroup.nativeElement[7].value;*/
   /*  this.email = "hola@gmail.com"//this.formGroup.nativeElement[8].value;/*/
     this.option = this.isSelected(this.selectedLink);

     console.log("Variable "+ this.option);
     console.log("Variable "+ this.suggestion);
     console.log("Variable "+ this.email);
     this.data = 
     {
          "tipo": this.option,
          "sugerencia": this.suggestion,
          "correo":this.email,
          "ubicion":"No leido",


      };


     this.postSugerencia(this._http);
      //this.formGroup.nativeElement[8]= "";
     //Limpio variable
     this.suggestion = "";
     this.email = "xzxxzx";
     this.option = "";
   
    }
    constructor(public  _http: HttpClient) {

      // this._http.post()
   
   
   
      }
    postSugerencia( _http: HttpClient){
      this._http.post('http://127.0.0.1:8000/postSugerencia/',this.data)
      .subscribe(
        data=>console.log(data)
        ,(err: HttpErrorResponse)=>{console.log("Un error ha ocurrido")}
        ,()=>console.log("solicitud finalizada OK")
        )
    }

   /* postNuevoTipoSugerencia( _http: HttpClient){
      this._http.post('http://127.0.0.1:8000/postTipoSugerencia/',this.tipo)
      .subscribe(
        data=>console.log(this.tipo)
        ,(err: HttpErrorResponse)=>{console.log("Un error ha ocurrido")}
        ,()=>console.log("solicitud finalizada OK")
        )
    }*/

     resetForm(formData: any, formDirective: FormGroupDirective): void {
      formDirective.resetForm();
      this.myForm.reset();
  }
  
    
  
}
