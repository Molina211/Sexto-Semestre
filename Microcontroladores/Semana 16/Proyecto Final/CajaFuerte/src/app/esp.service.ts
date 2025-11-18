import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

const API_BASE = "http://172.20.10.3:8000";

@Injectable({
  providedIn: 'root',
})
export class EspService {
  constructor(private http: HttpClient) {}

  getRegistros(): Observable<any[]> {
    return this.http.get<any[]>(`${API_BASE}/esp32/registros`);
  }

  stopBuzzer(): Observable<any> {
    return this.http.post(`${API_BASE}/esp32/buzzer/off`, {});
  }

  startBuzzer(): Observable<any> {
    return this.http.post(`${API_BASE}/esp32/buzzer/on`, {});
  }

  getBuzzerState(): Observable<any> {
    return this.http.get(`${API_BASE}/esp32/buzzer`);
  }
}
