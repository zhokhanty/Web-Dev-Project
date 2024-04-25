import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router'; // Import Router
import { LeagueService } from '../services/league.service';

@Component({
  selector: 'app-sign-up',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent {
  signUpForm: FormGroup;

  constructor(
    private fb: FormBuilder, 
    private api: LeagueService,
    private router: Router
  ) {
    this.signUpForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      first_name: ['', Validators.required],
      user_name: ['', Validators.required],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });
  }

  onSubmit() {
    if (this.signUpForm.valid) {
      const userData = this.signUpForm.value;
      console.log('Submitting user data:', userData);

      this.api.signUpUser(userData).subscribe(
        response => {
          console.log('Signup successful!', response);
          this.router.navigate(['/signin']);
        },
        error => {
          console.error('Signup failed!', error);
        }
      );
    } else {
      alert('Please fill in all required fields.'); // Show alert when form is invalid
    }
  }
}