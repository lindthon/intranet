import { Component, OnInit } from '@angular/core';
import { LoginService } from './login.service';
import { Router } from '@angular/router';
import { error } from 'console';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username: string;
  password: string;
  message: string;
  showErrorMessage: boolean;

  constructor(public service_login: LoginService, public router: Router) {}
  ngOnInit(): void {
    throw new Error("Method not implemented.");
  }

  login() {
    this.showErrorMessage = false;
    const user = {username: this.username, password: this.password};
    console.log(this.username);
    this.service_login.login(user).subscribe( data => {
      console.log(user.username);  
      this.service_login.setUser(user.username);  
      this.service_login.setToken(data.token);
      this.service_login.setLogin(true);
      this.service_login.getToken();
      this.router.navigateByUrl('/');
    },
    (error)=>{
      this.message="Usuario o contraseña incorrecta";
      console.log("error");
      this.showErrorMessage = true;

    }
    
    
    
    );
  }
}
  

