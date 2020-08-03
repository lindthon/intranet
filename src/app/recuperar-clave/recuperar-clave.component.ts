import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-recuperar-clave',
  templateUrl: './recuperar-clave.component.html',
  styleUrls: ['./recuperar-clave.component.css']
})
export class RecuperarClaveComponent implements OnInit {
  correo: string;
  data: any;
  showCorrectMessage:boolean;
  showErrorMessage:boolean;
  
  constructor(public _http:HttpClient) { 

  }

  ngOnInit(): void {
  }

  enviarCorrero(){
    this.data = 
    {
         "correo": this.correo,
     };
     console.log(this.correo);

     this.postRecuoerarClave(this._http);

  }

  postRecuoerarClave( _http: HttpClient){
    this.showErrorMessage=false;
    this.showCorrectMessage=false;
    this._http.post('http://127.0.0.1:8000/sendEmail/',this.data,{responseType: 'text'})
    .subscribe(
      (data)=>{console.log(data);
        this.showCorrectMessage=true
      }
      ,(err: HttpErrorResponse)=>{
        console.log(err.message)
        this.showErrorMessage=true;
      
      }
      ,()=>console.log("solicitud finalizada OK")
      )
  }

}
