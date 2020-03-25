import { Injectable } from '@angular/core'
import { Http, RequestOptions, Headers, Response} from '@angular/http'
import { Observable } from 'rxjs';
import { map } from "rxjs/operators";

// import { URL_API } from './app.api'
import { Client } from './shared/client.model'
import { HttpClient, HttpHeaders} from '@angular/common/http'

@Injectable()
export class CreateClient {
    constructor(private http: HttpClient){}
    public createNewClient(client: Client): Observable <object> {
        let headers = new HttpHeaders({
            'Content-Type': 'application/json'});
        let options = { headers: headers };

        return this.http.post(
            'http://localhost:8000/client/signup/',
            JSON.stringify(client),
            options)
        .pipe(
            map((response: Response) => response))
    } 
}
