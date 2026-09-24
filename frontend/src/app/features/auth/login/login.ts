import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router , RouterLink } from '@angular/router';

import { Auth } from '../../../core/services/auth';

@Component({
  selector: 'app-login',
  imports: [FormsModule,RouterLink],
  templateUrl: './login.html',
  styleUrl: './login.css'
})
export class Login {
  username = '';
  password = '';
  errorMessage = '';
  isLoading = false;

  constructor(
    private auth: Auth,
    private router: Router
  ) {}

  login(): void {
    this.errorMessage = '';

    if (!this.username || !this.password) {
      this.errorMessage = 'Username and password are required.';
      return;
    }

    this.isLoading = true;

    this.auth.login({
      username: this.username,
      password: this.password
    }).subscribe({
      next: (response) => {
        this.auth.saveToken(response.access_token);
        this.router.navigate(['/rooms']);
      },
      error: (error) => {
        this.isLoading = false;

        this.errorMessage =
          error.error?.message || 'Login failed. Please try again.';
      }
    });
  }
}