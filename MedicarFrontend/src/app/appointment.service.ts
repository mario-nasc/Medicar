import { Injectable } from '@angular/core'
import { Response} from '@angular/http'
import { Observable } from 'rxjs';
import { map } from "rxjs/operators";

// import { URL_API } from './app.api'
import { HttpClient, HttpHeaders} from '@angular/common/http'
import { AuthService } from './auth.service';

@Injectable()
export class Appointment {
    constructor(private http: HttpClient, private auth: AuthService){}
    public getAppointments(): Observable <object> {
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Authorization': `Token ${this.auth.getUser().token}`,});
        let options = { headers: headers };
        return this.http.get(
            'http://localhost:8000/api/appointment/', options)
        .pipe(
            map((response: Response) => response))
    }
    public deleteAppointment(id): Observable <object> {
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Authorization': `Token ${this.auth.getUser().token}`,});
        let options = { headers: headers };
        return this.http.delete(
            `http://localhost:8000/api/appointment/${id}`, options)
        .pipe(
            map((response: Response) => response))
    }
    public createAppointment(schedule_id, hour): Observable <object> {
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Authorization': `Token ${this.auth.getUser().token}`,});
        const body = {
            'agenda_id': schedule_id,
            'horario': hour
        }
        let options = { headers: headers };
        return this.http.post(
            'http://localhost:8000/api/appointment/',
            JSON.stringify(body),
            options)
        .pipe(
            map((response: Response) => response)
        )
    }
}
