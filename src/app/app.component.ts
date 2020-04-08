import { Component } from '@angular/core';
import { faClock,faMapMarkerAlt } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'IntranetIPSP';    
  faClock=faClock;
  faMapMarkerAlt=faMapMarkerAlt;
}
