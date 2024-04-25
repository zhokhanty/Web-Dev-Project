import { Component } from '@angular/core';
import { Team } from '../interfaces/team';
import { TeamsService } from '../services/teams.service';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { TopBarComponent } from '../top-bar/top-bar.component';
import { Player } from '../interfaces/player';

@Component({
  selector: 'app-team-details',
  standalone: true,
  imports: [RouterModule, CommonModule, TopBarComponent],
  templateUrl: './team-details.component.html',
  styleUrl: './team-details.component.css'
})
export class TeamDetailsComponent {
  team!: Team
  players: Player[] = []

  constructor(private api: TeamsService, private route: ActivatedRoute){}

  ngOnInit() {
    const id = Number(this.route.snapshot.paramMap.get('id'))
    this.api.getTeam(id).subscribe((data: Team) => {
      this.team = data

      if (this.team) {
        this.api.getPlayersInTeams(id).subscribe((playersData: Player[]) => {
          this.players = playersData;
        })
      }
    })

  }
}
