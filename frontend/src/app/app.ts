import { Component, signal } from '@angular/core';
import { CancionesComponent } from './canciones/canciones.component';
import { HttpClientModule } from '@angular/common/http';
@Component({
  selector: 'app-root',
  imports: [CancionesComponent, HttpClientModule],
  templateUrl: './app.html',
  styleUrl: './app.css',
  standalone: true,

})
export class App {
  protected readonly title = signal('frontend');
}
