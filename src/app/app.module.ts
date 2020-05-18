import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule } from '@angular/forms';

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
import { IgxCalendarModule } from 'igniteui-angular';
import {Ng2SmartTableModule} from 'ng2-smart-table';

import { SugerenciasComponent } from './sugerencias/sugerencias.component';
import { ReglamentoComponent } from './reglamento/reglamento.component';
import { DirectorioComponent } from './directorio/directorio.component';

import { HashLocationStrategy, LocationStrategy  } from '@angular/common';

@NgModule({
  declarations: [
    AppComponent,
    IndexComponent,
    HeaderComponent,
    FooterComponent,
    NoticiasComponent,
    CarrouselComponent,
    CategoriaNoticiasComponent,
    NoticiaComponent,
    EventosComponent,
    CalendarComponent,
    SugerenciasComponent,
    ReglamentoComponent,
    DirectorioComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    FormsModule,
    NgxPaginationModule,
    FontAwesomeModule,
    BrowserAnimationsModule,
    IgxCalendarModule,
    Ng2SmartTableModule
  ],
  providers: [
    {provide : LocationStrategy , useClass: HashLocationStrategy}
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
