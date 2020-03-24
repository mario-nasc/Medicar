import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(private Auth: AuthService, private router:Router) { }

  getRememberMe(){
    let rememberMe = JSON.parse(localStorage.getItem('rememberMe'))
    if(rememberMe == true){
      let oldusername = localStorage.getItem('username' || '')
      let username = (<HTMLInputElement>document.getElementById('username'))
      username.value = oldusername
    }
  }

  ngOnInit(){
    this.getRememberMe()
  }

  showPassword() {
    var field = (<HTMLInputElement>document.getElementById("password"))
    if (field.type === "password") {
      field.type = "text";
    } else {
      field.type = "password";
    }
  }

  loginUser(event){
    event.preventDefault()
    const target = event.target
    const username = target.querySelector('#username').value
    const password = target.querySelector('#password').value
    const rememberme = target.querySelector('#rememberme').checked

    // Reference to "lembre me" checkbox
    if (rememberme == true){
      localStorage.setItem('rememberMe', 'true');
      localStorage.setItem('username', username);
    }else{
      localStorage.removeItem('rememberMe');
      localStorage.removeItem('username');
    }

    // if auth go to home else stay in this view
    this.Auth.getUserDetails(username, password).subscribe(
      (data) => {
          this.router.navigate([''])
          this.Auth.setLoggedIn(true)
      },
      (data) => {
        console.log('error', data.status)
      }
    )
  }
}
