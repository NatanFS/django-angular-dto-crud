import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { MatSidenav, MatSidenavModule } from '@angular/material/sidenav';
import { NavComponent } from './nav/nav.component';
import { HttpClientModule } from '@angular/common/http';
import { PersonService } from './person/person.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule, 
    NavComponent,
    HttpClientModule
  ],
  providers: [
    PersonService
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'athenas';
}
