import { Injectable } from '@angular/core'
import { Response} from '@angular/http'
import { Observable } from 'rxjs';
import { map } from "rxjs/operators";

// import { URL_API } from './app.api'
import { HttpClient, HttpHeaders} from '@angular/common/http'
import { AuthService } from './auth.service';

@Injectable()
export class SpecialtyService {
    constructor(private http: HttpClient, private auth: AuthService){}
    public getSpecialties(): Observable <object> {
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Authorization': `Token ${this.auth.getUser().token}`,});
        let options = { headers: headers };
        return this.http.get(
            'http://localhost:8000/api/specialty/', options)
        .pipe(
            map((response: Response) => response))
    } 
}
