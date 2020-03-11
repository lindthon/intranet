import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IndexComponent } from './index/index.component';
import { NoticiasComponent } from './noticias/noticias.component';


const routes: Routes = [
  { path: "",component:IndexComponent},
  { path: "noticias",component:NoticiasComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents =[IndexComponent,NoticiasComponent]
