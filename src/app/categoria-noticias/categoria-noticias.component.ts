import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpResponse, HttpErrorResponse } from '@angular/common/http';
import { ActivatedRoute,Params, RouterEvent, NavigationEnd, Router } from '@angular/router';
import { filter, takeUntil } from 'rxjs/operators';
import { Subject } from 'rxjs';

@Component({
  selector: 'app-categoria-noticias',
  templateUrl: './categoria-noticias.component.html',
  styleUrls: ['./categoria-noticias.component.css']
})
export class CategoriaNoticiasComponent implements OnInit {

  news:any=[{
    "image":"assets/img/planta/camarones.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Cambios políticos",
    "id":"1",
    "title":"Titulo de Camarones",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/maquina.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Cambios políticos",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/sistema.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Cambios políticos",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/contenedor.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Cambios políticos",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/camarones.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Cambios políticos",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/sistema.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Cambios políticos",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/maquina.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Cambios políticos",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/contenedor.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Cambios políticos",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/camarones.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Cambios políticos",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/contenedor.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Cambios políticos",
    "id":"1",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  }
]
public destroyed = new Subject<any>();
  cate: any;
  categorias=[];

  noti: any;
  noticias=[];
  id: any;
  categoria: any;
  constructor(private _http: HttpClient,public activatedRoute: ActivatedRoute, public router: Router) { 
    this.getCategorias(this._http);

  }
  p:number =1;
  ngOnInit(): void {
   // this.getTodasLasNoticiasByID(this._http);
    this.categoria = this.activatedRoute.snapshot.params['categoria'];

    this.activatedRoute.paramMap.subscribe(params => {
      this.id = params.get("id");
      this.categoria = this.activatedRoute.snapshot.params['categoria'];
      this.getTodasLasNoticiasByID(this._http);
      this.noticias=[];

   })
  }
  ngOnDestroy(): void {
    this.destroyed.next();
    this.destroyed.complete();
  }
 

  getTodasLasNoticiasByID(_http:HttpClient){
    this.id = this.activatedRoute.snapshot.params['id'];

    this._http.get('http://127.0.0.1:8000/getTodasLasNoticiasByID/?id='+this.id)
    .subscribe(
      (data)=>{console.log(data);
        this.noti=data;
        for (let key in this.noti) {
          let notica = this.noti[key];
          console.log(notica);
          this.noticias.push(notica);
      }   
      }
      ,(err: HttpErrorResponse)=>{console.log("Un error ha ocurrido")}
      ,()=>console.log("solicitud finalizada OK")
      )
  }
  getCategorias(_http:HttpClient){
    this._http.get('http://127.0.0.1:8000/getCategoria/')
    .subscribe(
      (data)=>{console.log(data);
        this.cate=data;
        for (let key in this.cate) {
          let cate = this.cate[key];
          console.log(cate);
          this.categorias.push(cate);
      }   
      }
      ,(err: HttpErrorResponse)=>{console.log("Un error ha ocurrido")}
      ,()=>console.log("solicitud finalizada OK")
      )
  }

}
