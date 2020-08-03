import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable} from 'rxjs';
import { CookieService } from "ngx-cookie-service";

@Injectable({
  providedIn: "root"
})
export class LoginService {
  isLoggedIn = false;

  constructor(private http: HttpClient, private cookies: CookieService) {}

  login(user: any): Observable<any> {
    //return this.http.post("https://reqres.in/api/login", user);    
    return this.http.post("http://127.0.0.1:8000/api-token-auth/", user);
      //return this.http.post("http://127.0.0.1:8000/login/", user);

  }
  setUser(name: string){
    localStorage.setItem('user', name);

  }

  setToken(token: string) {
    localStorage.setItem('token', token);
    this.cookies.set("token", token);
  }
  setLogin(isLoggedIn: boolean) {
    this.isLoggedIn=isLoggedIn;
    
  }
  public logout(){
    localStorage.removeItem("token");
    localStorage.clear();
  }
  getToken() {
    const token_parts = this.cookies.getAll;
    console.log(token_parts)
    return this.cookies.get("token");
  }
}