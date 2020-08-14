import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { AnyTxtRecord } from 'dns';
import {NgForm, Validators, FormGroup} from '@angular/forms';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.css']
})
export class PerfilComponent implements OnInit {
  constructor(public _http:HttpClient) {
    console.log(localStorage.getItem("user"));
   }

 
  cedula: string;
  nombre: string ="xyz";
  apellido:string;
  correo:string;
  image:string;
  fecha:any;
  url=null;
  default='https://www.w3schools.com/howto/img_avatar.png';
  /*Actualizar Info*/

  data:any;
  name: string ="xx";
  last_name: string;
  mail: string;
  id: string;
  new_image: any;
  born: any;
  
  usuarios = [];
  getByUserName(_http: HttpClient){
    this._http.get('http://127.0.0.1:8000/get_user/?id='+localStorage.getItem("user"))
    .subscribe(
      (data)=>{console.log(data);
        console.log(data['correo'])
        this.cedula=data['cedula'];
        this.nombre=data['nombre'];
        this.apellido=data['apellido'];
        this.correo=data['correo'];
        this.image=data['img'];
        this.fecha=data['fecha'];

        this.name=data['nombre'];
        this.last_name=data['apellido'];
        this.mail=data['correo'];
        this.id=localStorage.getItem("user");
        this.data = {
          "first_name":this.name,
          "last_name":this.last_name,
          "mail":this.mail,
          "image":this.new_image,
          "extension":"1111",
          "fecha":this.born,
          "id":localStorage.getItem("user"),
        }



      }
      ,(err: HttpErrorResponse)=>{console.log("Un error ha ocurrido")}
      ,()=>console.log("solicitud finalizada OK")
      )
  }
  
  ngOnInit(): void {
    this.getByUserName(this._http);
    setTimeout(() => {
      this.name=this.nombre;
      //this.updateInfo();
      console.log('userId is:',this.name);  // You will get the @Input value
    });
    if (this.name === null || this.name === undefined) {
      throw new TypeError("The input ‘Person’ is required");
    }
    console.log("xxxxxxxxxxxxxxxxxxx")
    console.log(this.name);
   
  }
  ngAfterViewInit():	void{
    this.getByUserName(this._http);

  }

  onSubmit(f: NgForm) {
    console.log("aqui form")
    console.log(f.value);  // { first: '', last: '' }
    console.log(f.valid);  // false
  }
  reload(){
    console.log("reload")
    this.getByUserName(this._http);
  }


password: any;
confirmation: any;
coincidenFlag: boolean=null;
  checkIfMatchingPasswords() {
        if(this.password===this.confirmation && this.password!=null && this.confirmation!=null){
          this.upadatePassword();
          this.coincidenFlag=true;
        }else{
          this.coincidenFlag=false;
        }
    }
  upadatePassword(){
    const data = {"password":this.password, "id":localStorage.getItem("user")}
    this._http.post('http://127.0.0.1:8000/upadatePassUser/',data)
    .subscribe(
      (data)=>{console.log(data)
        console.log("Solicitud enviada correctamente OK")
      },
      (err:HttpErrorResponse)=>{
        console.log(err)
      }
    )
  }

  updateInfo(){
    console.log("Actualizando info...")
    this.data = {
      "first_name":this.name,
      "last_name":this.last_name,
      "mail":this.mail,
      "image":this.new_image,
      "extension":"1111",
      "fecha":this.born,
      "id":localStorage.getItem("user"),
    }
    this.updateDataUser(this._http);
    console.log("actulializado")
  }
  updateDataUser(_http: HttpClient){
   
    console.log(this.data);

   this._http.post('http://127.0.0.1:8000/postDataUser/', this.data)
    .subscribe(
      (data)=>{console.log(data)
        console.log("Solicitud enviada correctamente OK")
      },
      (err:HttpErrorResponse)=>{
        console.log(err)
      }
    )
  }

}
