import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EspService } from './esp.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  title = 'Caja Fuerte';
  registros: any[] = [];
  loading = false;
  message = '';

  constructor(private esp: EspService) {}

  ngOnInit(): void {
    this.load();
  }

  load(): void {
    this.loading = true;
    this.message = '';
    this.esp.getRegistros().subscribe({
      next: (data) => {
        this.registros = data || [];
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.message = 'Error al cargar registros';
        this.loading = false;
      },
    });
  }

  apagarAlarma(): void {
    this.message = '';
    this.esp.stopBuzzer().subscribe({
      next: (_) => {
        this.message = 'Alarma apagada (servidor)';
        // refrescar lista para ver cambios si los hay
        this.load();
      },
      error: (err) => {
        console.error(err);
        this.message = 'Error al apagar alarma';
      },
    });
  }
}
