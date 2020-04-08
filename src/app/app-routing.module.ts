import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IndexComponent } from './index/index.component';
import { NoticiasComponent } from './noticias/noticias.component';
import { NoticiaComponent } from './noticia/noticia.component';
import { EventosComponent } from './eventos/eventos.component';
import { CategoriaNoticiasComponent } from './categoria-noticias/categoria-noticias.component';


const routes: Routes = [
  { path: "",component:IndexComponent},
  { path: "noticias",component:NoticiasComponent},
  { path: "categoria-noticias",component:CategoriaNoticiasComponent},
  { path: "noticia",component:NoticiaComponent},
  { path: "eventos",component:EventosComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents =[IndexComponent,NoticiasComponent]
