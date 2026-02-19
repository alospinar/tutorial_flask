import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Cancion } from './cancion';
import { CancionesService } from './canciones.service';

@Component({
  selector: 'app-canciones',
  templateUrl: './canciones.component.html',
  styleUrls: ['./canciones.component.css'],
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  providers: [CancionesService]
})
export class CancionesComponent {
  canciones: Array<Cancion> = [];

  constructor(private cancionesService: CancionesService) {
    this.cargarCanciones();
  }

  cargarCanciones() {
    this.cancionesService.getCanciones().subscribe({
      next: (data) => {
        this.canciones = data;
        console.log('Canciones cargadas:', data);
      },
      error: (error) => {
        console.error('Error al cargar canciones:', error);
      }
    });
  }
}
