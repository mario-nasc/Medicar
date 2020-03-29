import { Component, OnInit, ViewChild} from '@angular/core';
import { Router } from '@angular/router';
import { Client } from '../shared/client.model'
import { CreateClient } from '../create-client.service';
import { FormGroup, FormControl, Validators, AbstractControl, FormBuilder } from '@angular/forms';


@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss'],
  providers: [ CreateClient ]
})
export class RegistrationComponent implements OnInit {
    
    public registrationForm: FormGroup;

    constructor(
        private router: Router,
        private createClient: CreateClient,
    ) {}

    ngOnInit() {
      this.registrationForm = new FormGroup({});
      this.registrationForm.addControl('name', new FormControl('', [Validators.required, Validators.minLength(6)]));
      this.registrationForm.addControl('email', new FormControl('', [Validators.required, Validators.pattern("^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$")]));
      this.registrationForm.addControl('password', new FormControl('', [Validators.required, Validators.minLength(8)]));
      this.registrationForm.addControl('confirm_password', new FormControl(
          '', [Validators.compose(
              [Validators.required, this.validateAreEqual.bind(this)]
          )]
      ));
    }

    private validateAreEqual(fieldControl: FormControl) {
      return fieldControl.value === this.registrationForm.get("password").value ? null : {
          NotEqual: true
      };
    }
    showPassword() {
      let field = (<HTMLInputElement>document.getElementById("insertPassword"))
      let icon = (<HTMLInputElement>document.getElementById("passwordIcon"))
      if (field.type === "password") {
        field.type = "text";
        icon.className = 'fa fa-fw fa-eye-slash field-icon toggle-password';
      } else {
        field.type = "password";
        icon.className = 'fa fa-fw fa-eye field-icon toggle-password';
      }
    }
    showConfirmPassword() {
      let field = (<HTMLInputElement>document.getElementById("confirmPassword"))
      let icon = (<HTMLInputElement>document.getElementById("confirmPasswordIcon"))
      if (field.type === "password") {
        field.type = "text";
        icon.className = 'fa fa-fw fa-eye-slash field-icon toggle-password';
      } else {
        field.type = "password";
        icon.className = 'fa fa-fw fa-eye field-icon toggle-password';
      }
    }

    registerUser(): void {
        
        let client = new Client(
          this.registrationForm.value.name,
          this.registrationForm.value.password,
          this.registrationForm.value.email,
        )
        this.createClient.createNewClient(client)
        .subscribe((response: Object) => {
          alert("Usuário Cadastrado com Sucesso")
          this.router.navigate(['login'])
        }, (error: any) => {
          alert(error.error[Object.keys(error.error)[0]])
        })
    }
}
