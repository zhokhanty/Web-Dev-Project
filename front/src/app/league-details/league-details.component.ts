import { Component } from '@angular/core';
import { League } from '../interfaces/league';
import { LeagueService } from '../services/league.service';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-league-details',
  standalone: true,
  imports: [RouterModule, CommonModule],
  templateUrl: './league-details.component.html',
  styleUrl: './league-details.component.css'
})
export class LeagueDetailsComponent {
  league!: League

  constructor(private api: LeagueService, private route: ActivatedRoute){}

  ngOnInit() {
    const id = Number(this.route.snapshot.paramMap.get('id'))
    this.api.getLeague(id).subscribe((data: League) => {
      this.league = data

      
    })
  }

}
