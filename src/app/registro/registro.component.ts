import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit {
  username: string;
  password: string;
  correo: string;
  nombres: string;
  apellidos: string;
  cedula: string;
  fecha: string;
  extension: string;

  showErrorMessage: boolean;
  constructor() { }

  ngOnInit(): void {
  }

}
