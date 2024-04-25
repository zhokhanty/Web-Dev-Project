import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Team } from '../interfaces/team';
import { Player } from '../interfaces/player';
import { Coach } from '../interfaces/coach';

@Injectable({
  providedIn: 'root'
})
export class TeamsService {
  private url = 'http://127.0.0.1:8000/api/';

  constructor(private http: HttpClient) { }

  getTeam(id: number): Observable<Team> {
    return this.http.get<Team>(`${this.url}${'teams/'}${id}${'/'}`)
  }

  getPlayersInTeams(id: number): Observable<Player[]> {
    return this.http.get<Player[]>(`${this.url}${'teams/'}${id}${'/players/'}`)
  }
  getCoachInTeams(id: number): Observable<Coach> {
    return this.http.get<Coach>(`${this.url}${'coaches/'}${id}${'/teams/'}`)
  }
}
