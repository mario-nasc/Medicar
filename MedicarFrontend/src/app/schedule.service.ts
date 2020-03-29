import { Injectable } from '@angular/core'
import { Response} from '@angular/http'
import { Observable } from 'rxjs';
import { map } from "rxjs/operators";

// import { URL_API } from './app.api'
import { HttpClient, HttpHeaders, HttpParams} from '@angular/common/http'
import { AuthService } from './auth.service';

@Injectable()
export class ScheduleService {
    constructor(private http: HttpClient, private auth: AuthService){}
    public getSchedulesWithDoctor(doctor_id): Observable <object> {
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Authorization': `Token ${this.auth.getUser().token}`,});
        let params = new HttpParams();
        params = params.append('medico', doctor_id)
        let schedule_url = 'http://localhost:8000/api/schedule/'
        return this.http.get<any>(schedule_url,  { headers, params })
        .pipe(
            map((response: Response) => response))
    }
}
