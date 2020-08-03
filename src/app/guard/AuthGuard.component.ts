import { CanActivate, RouterStateSnapshot, ActivatedRouteSnapshot, Router } from '@angular/router';
import { Injectable } from '@angular/core';
import { LoginService } from '../login/login.service';

@Injectable({
    providedIn: 'root'
  })
  export class AuthGuard implements CanActivate {
    constructor(public service_login: LoginService , private router: Router) {}
  
    canActivate(next: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        if (localStorage.getItem("token")==null) {
          // redirect to some view explaining what happened
          this.router.navigateByUrl('login');
          
          return false;
        } else {
          console.log("nlogeadooo....");
          console.log(localStorage.getItem("token"));
          return true;
        }
      }

     
  }