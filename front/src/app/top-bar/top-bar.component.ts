import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';

@Component({
  selector: 'app-top-bar',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './top-bar.component.html',
  styleUrl: './top-bar.component.css'
})
export class TopBarComponent {
  constructor(private router: Router) { }
  navigateToSignUp() {
    
    this.router.navigate(['signup']);
  }

  navigateToSignIn(){
      this.router.navigate(['signin']);
  }
}
