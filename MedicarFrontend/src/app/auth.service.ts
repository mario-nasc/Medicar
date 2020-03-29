import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http'
import { User } from './shared/user.model'

@Injectable()
export class AuthService {

  private loggedInStatus = JSON.parse(localStorage.getItem('loggedIn') || 'false')
  private user = null

  constructor(private http: HttpClient) { }

  setLoggedIn(value: boolean){
    this.loggedInStatus = value
    localStorage.setItem('loggedIn', value.toString())
    localStorage.setItem('token', this.user.token)
    localStorage.setItem('userid', this.user.userid)
    localStorage.setItem('username', this.user.username)
  }

  get isLoggedIn(){
    return JSON.parse(localStorage.getItem('loggedIn') || this.loggedInStatus.toString())
  }

  getUserDetails(username, password){
    return this.http.post('http://localhost:8000/client/login/', {
      "username": username,
      "password": password
    })
  }

  getUser() {
    return this.user
  }
  
  setUser(userid, token, name) {
    this.user = new User(
      userid,
      token,
      name
    )
  }
}
