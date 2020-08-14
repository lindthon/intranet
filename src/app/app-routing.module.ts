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
import { LoginComponent } from './login/login.component';
import { RecuperarClaveComponent } from './recuperar-clave/recuperar-clave.component';
import { BrigadasComponent } from './brigadas/brigadas.component';
import { EmpleadosComponent } from './empleados/empleados.component';
import { AuthGuard } from './guard/AuthGuard.component';
import { PerfilComponent } from './perfil/perfil.component';
import {RegistroComponent} from './registro/registro.component';


const routes: Routes = [
  { path: "",component:IndexComponent,canActivate: [AuthGuard]},
  { path: "login",component:LoginComponent},
  { path: "recuperar-clave",component:RecuperarClaveComponent},
  { path: "perfil",component:PerfilComponent,canActivate: [AuthGuard]},
  { path: "brigadas",component:BrigadasComponent,canActivate: [AuthGuard]},
  { path: "empleados",component:EmpleadosComponent,canActivate: [AuthGuard]},
  { path: "noticias",component:NoticiasComponent,canActivate: [AuthGuard]},
  { path: "categoria-noticias/:id/:categoria",component:CategoriaNoticiasComponent, pathMatch: 'full',canActivate: [AuthGuard]},
  { path: "noticia/:id/details",component:NoticiaComponent, pathMatch: 'full',canActivate: [AuthGuard]},
  { path: "eventos",component:EventosComponent,canActivate: [AuthGuard]},
  { path: "calendario",component:CalendarComponent,canActivate: [AuthGuard]},
  { path: "sugerencias",component:SugerenciasComponent,canActivate: [AuthGuard]},
  { path: "reglamento",component:ReglamentoComponent,canActivate: [AuthGuard]},
  { path: "directorio",component:DirectorioComponent,canActivate: [AuthGuard]},
  { path: "registro",component:RegistroComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes,{onSameUrlNavigation: 'reload'})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents =[IndexComponent,NoticiasComponent,BrigadasComponent]
