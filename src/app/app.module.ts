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

import { CalendarModule, DateAdapter } from 'angular-calendar';
import { adapterFactory } from 'angular-calendar/date-adapters/date-fns';
import { SugerenciasComponent } from './sugerencias/sugerencias.component';
import { ReglamentoComponent } from './reglamento/reglamento.component';
import { DirectorioComponent } from './directorio/directorio.component';

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
    CalendarModule.forRoot({
      provide: DateAdapter,
      useFactory: adapterFactory,
    }),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
