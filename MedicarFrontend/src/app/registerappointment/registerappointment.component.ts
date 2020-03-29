import { Component, OnInit, ViewChild } from '@angular/core';
import { SpecialtyService } from '../specialty.service';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { DoctorService } from '../doctor.service';
import { ScheduleService } from '../schedule.service';
import { Appointment } from '../appointment.service';

@Component({
  selector: 'app-registerappointment',
  templateUrl: './registerappointment.component.html',
  styleUrls: ['./registerappointment.component.scss'],
  providers: [ SpecialtyService, DoctorService, ScheduleService, Appointment, Map ]
})
export class RegisterappointmentComponent implements OnInit {
  public specialties: Array<any>
  public doctors: Array<any>
  public schedules: Array<any>
  public registrationForm: FormGroup;

  constructor(
    private specialty: SpecialtyService,
    private doctor: DoctorService,
    private schedule: ScheduleService,
    public hours: Map<string,Array<string>>,
    private appointment: Appointment,
    private route: Router
    )
    { }

  ngOnInit(): void {
    this.specialty.getSpecialties()
    .subscribe(
      (response: any) => {
        this.specialties = response
      },
      (error: any) => console.log('deu errado')
    )
    this.registrationForm = new FormGroup({});
    this.registrationForm.addControl('specialty', new FormControl('', [Validators.compose(
      [Validators.required, this.validateNotDefaultValue.bind(this)])]));
    this.registrationForm.addControl('doctor', new FormControl('', [Validators.compose(
      [Validators.required, this.validateNotDefaultValue.bind(this)])]));
    this.registrationForm.addControl('date', new FormControl('', [Validators.compose(
      [Validators.required, this.validateNotDefaultValue.bind(this)])]));
    this.registrationForm.addControl('hour', new FormControl('', [Validators.compose(
      [Validators.required, this.validateNotDefaultValue.bind(this)])]));
  }
  private validateNotDefaultValue(fieldControl: FormControl) {
    return fieldControl.value === '' ? {defaultValue: true} : null;
  }
  getDoctors(): void {
    this.doctor.getDoctorsWithSpecialty(this.registrationForm.controls.specialty.value)
    .subscribe(
      (response: any) => {
        this.doctors = response
      },
      (error: any) => {
        console.log('error', error)
      }
    )
    this.schedules = []
    this.hours = new Map<string, Array<string>>()
  }
  getSchedules(): void {
    this.schedule.getSchedulesWithDoctor(this.registrationForm.controls.doctor.value)
    .subscribe(
      (response: any) => {
        this.schedules = response
        response.forEach(element => {
          let schedule_hours: Array<string> = []
          element.horarios.forEach(hours => {
            schedule_hours.push(hours.horario)
          })
          this.hours.set(element.id, schedule_hours)
        });
      console.log(this.hours)},
      (error: any) => {
        console.log(error)
      }
    )
  }
  registerAppointment(): void {
    console.log(this.registrationForm)
    console.log(this.registrationForm.value.hour)
    console.log(this.registrationForm.value.date)
    this.appointment.createAppointment(
      this.registrationForm.value.date,
      this.registrationForm.value.hour)
    .subscribe(
      (response:any) => {
        console.log('response', response)
        alert("Consulta cadastrada com Sucesso")
        location.reload()
      },
        (error: any) => console.log('error', error)
    )
    console.log('create')
  }

}
