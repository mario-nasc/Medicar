import { Injectable } from '@angular/core'
import { Response} from '@angular/http'
import { Observable } from 'rxjs';
import { map } from "rxjs/operators";

// import { URL_API } from './app.api'
import { HttpClient, HttpHeaders, HttpParams} from '@angular/common/http'
import { AuthService } from './auth.service';

@Injectable()
export class DoctorService {
    constructor(private http: HttpClient, private auth: AuthService){}
    public getDoctorsWithSpecialty(specialty_id): Observable <object> {
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Authorization': `Token ${this.auth.getUser().token}`,});
        let params = new HttpParams();
        params = params.append('especialidade', specialty_id)
        let doctor_url = 'http://localhost:8000/api/doctor'
        return this.http.get<any>(doctor_url,  { headers, params })
        .pipe(
            map((response: Response) => response))
    } 
}
