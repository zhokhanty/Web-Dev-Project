import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { LeagueService } from '../services/league.service';
import { League } from '../interfaces/league';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [RouterModule, CommonModule],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.css'
})
export class HomePageComponent {
  leagues: League[] = []

  constructor(private api: LeagueService){}

  ngOnInit(){
    this.api.getLeagues().subscribe((data) => {
      this.leagues = data
    })
  }
}
