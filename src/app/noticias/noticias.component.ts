import { Component, OnInit, ViewChild } from '@angular/core';
import { NgbCarousel, NgbSlideEvent, NgbSlideEventSource } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-noticias',
  templateUrl: './noticias.component.html',
  styleUrls: ['./noticias.component.css']
})
export class NoticiasComponent implements OnInit {

  images = [62, 83, 466, 965, 982, 1043, 738].map((n) => `https://picsum.photos/id/${n}/900/500`);

  paused = false;
  unpauseOnArrow = false;
  pauseOnIndicator = false;
  pauseOnHover = true;

  ultimos:any=[{
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
    "cat":"Brigada Médica",
    "id":"2",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/sistema.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Promoción",
    "id":"3",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  }]

  cambios:any=[{
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
    "id":"2",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/sistema.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Cambios políticos",
    "id":"3",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  }]

  Brigada:any=[{
    "image":"assets/img/planta/camarones.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Brigada Médica",
    "id":"1",
    "title":"Titulo de Camarones",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/maquina.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Brigada Médica",
    "id":"2",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  },
  {
    "image":"assets/img/planta/sistema.jpeg",
    "date":"MAY 8, 2018",
    "cat":"Brigada Médica",
    "id":"3",
    "title":"Global Travel And Vacations Luxury Travel On A Tight Budget",
    "descr":"Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum. Sed ut perspiciatis lorem150"
  }]

  constructor() { }

  ngOnInit(): void {
  }

  

  @ViewChild('carousel', {static : true}) carousel: NgbCarousel;

  togglePaused() {
    if (this.paused) {
      this.carousel.cycle();
    } else {
      this.carousel.pause();
    }
    this.paused = !this.paused;
  }

  onSlide(slideEvent: NgbSlideEvent) {
    if (this.unpauseOnArrow && slideEvent.paused &&
      (slideEvent.source === NgbSlideEventSource.ARROW_LEFT || slideEvent.source === NgbSlideEventSource.ARROW_RIGHT)) {
      this.togglePaused();
    }
    if (this.pauseOnIndicator && !slideEvent.paused && slideEvent.source === NgbSlideEventSource.INDICATOR) {
      this.togglePaused();
    }
  }
}
