import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IndexComponent } from './index/index.component';
import { NoticiasComponent } from './noticias/noticias.component';
import { NoticiaComponent } from './noticia/noticia.component';
import { CategoriaNoticiasComponent } from './categoria-noticias/categoria-noticias.component';
import { EventosComponent } from './eventos/eventos.component';
import { CalendarComponent } from './calendar/calendar.component';
import { SugerenciasComponent } from './sugerencias/sugerencias.component';
import { ReglamentoComponent } from './reglamento/reglamento.component';
import { DirectorioComponent } from './directorio/directorio.component';



const routes: Routes = [
  { path: "",component:IndexComponent},
  { path: "noticias",component:NoticiasComponent},
  { path: "categoria-noticias",component:CategoriaNoticiasComponent},
  { path: "noticia/:id/details",component:NoticiaComponent, pathMatch: 'full'},
  { path: "eventos",component:EventosComponent},
  { path: "calendario",component:CalendarComponent},
  { path: "sugerencias",component:SugerenciasComponent},
  { path: "reglamento",component:ReglamentoComponent},
  { path: "directorio",component:DirectorioComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents =[IndexComponent,NoticiasComponent]
