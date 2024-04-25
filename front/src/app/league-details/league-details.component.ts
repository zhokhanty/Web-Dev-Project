import { Component } from '@angular/core';
import { League } from '../interfaces/league';
import { LeagueService } from '../services/league.service';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { Team } from '../interfaces/team';
import { CommonModule } from '@angular/common';
import { HomePageComponent } from '../home-page/home-page.component';


@Component({
  selector: 'app-league-details',
  standalone: true,
  imports: [RouterModule, CommonModule, HomePageComponent],
  templateUrl: './league-details.component.html',
  styleUrls: ['./league-details.component.css']
})
export class LeagueDetailsComponent {
  league!: League;
  teams: Team[] = [];
  tournamentResults: { homeTeam: Team; awayTeam: Team; homeScore: number; awayScore: number }[] = [];

  constructor(private api: LeagueService, private route: ActivatedRoute) {}

  ngOnInit() {
    const leagueId = Number(this.route.snapshot.paramMap.get('id'));
    this.api.getLeague(leagueId).subscribe((data: League) => {
      this.league = data;

      if (this.league) {
        this.api.getTeamsInLeague(leagueId).subscribe((teamsData: Team[]) => {
          this.teams = teamsData;
          this.generateTournament(leagueId);
        });
      }
    });
    this.api.getTeams().subscribe((data) => {
      this.teams = data
    })
  }

  generateTournament(leagueId: number) {
    this.tournamentResults = [];
    
    const leagueTeams = this.teams.filter(team => team.league === leagueId);

    for (let i = 0; i < leagueTeams.length; i++) {
      for (let j = i + 1; j < leagueTeams.length; j++) {
        const homeTeam = leagueTeams[i];
        const awayTeam = leagueTeams[j];
        const homeScore = Math.floor(Math.random() * 6);
        const awayScore = Math.floor(Math.random() * 6);
        this.tournamentResults.push({ homeTeam, awayTeam, homeScore, awayScore });
      }
    }
  }
}
