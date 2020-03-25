import { Component, OnInit, ViewChild} from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators, NgForm } from '@angular/forms';
import { Client } from '../shared/client.model'
import { CreateClient } from '../create-client.service';


@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss'],
  providers: [ CreateClient ]
})
export class RegistrationComponent implements OnInit {
    @ViewChild('registration') public myform: NgForm

    constructor(
        private router: Router,
        private createClient: CreateClient
    ) {}

    ngOnInit() {
    }

    showPassword() {
      var field = (<HTMLInputElement>document.getElementById("insertPassword"))
      if (field.type === "password") {
        field.type = "text";
      } else {
        field.type = "password";
      }
    }
    showConfirmPassword() {
      var field = (<HTMLInputElement>document.getElementById("confirmPassword"))
      if (field.type === "password") {
        field.type = "text";
      } else {
        field.type = "password";
      }
    }

    registerUser(): void {
        let client = new Client(
          this.myform.value.name,
          this.myform.value.password,
          this.myform.value.email,
          
        )
        console.log(client)
        this.createClient.createNewClient(client)
        .subscribe((response: Object) => {
          alert("Usuário Cadastrado com Sucesso")
          this.router.navigate(['login'])
        }, (error: Object) => {
          alert(error.error[Object.keys(error.error)[0]])
        })
    }
}
