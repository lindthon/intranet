import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IndexComponent } from './index/index.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { NoticiasComponent } from './noticias/noticias.component';
import { CarrouselComponent } from './carrousel/carrousel.component';

import { CategoriaNoticiasComponent } from './categoria-noticias/categoria-noticias.component';
import { NoticiaComponent } from './noticia/noticia.component';
import { NgxPaginationModule } from 'ngx-pagination';
import { EventosComponent } from './eventos/eventos.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { CalendarComponent } from './calendar/calendar.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { IgxCalendarModule, IgxIconModule } from 'igniteui-angular';
import {Ng2SmartTableModule} from 'ng2-smart-table';

import { SugerenciasComponent } from './sugerencias/sugerencias.component';
import { ReglamentoComponent } from './reglamento/reglamento.component';
import { DirectorioComponent } from './directorio/directorio.component';

import { HttpClientModule } from '@angular/common/http';

import { HashLocationStrategy, LocationStrategy  } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { CookieService } from 'ngx-cookie-service';
import { BrigadasComponent } from './brigadas/brigadas.component';
import { EmpleadosComponent } from './empleados/empleados.component';
import { RecuperarClaveComponent } from './recuperar-clave/recuperar-clave.component';
import { PerfilComponent } from './perfil/perfil.component';
import { RegistroComponent } from './registro/registro.component';


@NgModule({
  declarations: [
    AppComponent,
    IndexComponent,
    HeaderComponent,
    FooterComponent,
    CarrouselComponent,
    CategoriaNoticiasComponent,
    NoticiaComponent,
    EventosComponent,
    CalendarComponent,
    SugerenciasComponent,
    ReglamentoComponent,
    DirectorioComponent,
    LoginComponent,
    BrigadasComponent,
    NoticiasComponent,
    EmpleadosComponent,
    RecuperarClaveComponent,
    PerfilComponent,
    RegistroComponent,
  ],
  imports: [
    IgxIconModule,
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    FormsModule,
    NgxPaginationModule,
    FontAwesomeModule,
    BrowserAnimationsModule,
    IgxCalendarModule,
    Ng2SmartTableModule,
    RouterModule,
    HttpClientModule
  ],
  providers: [CookieService,
    {provide : LocationStrategy , useClass: HashLocationStrategy}
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
