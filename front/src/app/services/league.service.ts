import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { League } from '../interfaces/league';
import { Team } from '../interfaces/team';
import { User } from '../interfaces/user';

@Injectable({
  providedIn: 'root'
})
export class LeagueService {
  private url = 'http://127.0.0.1:8000/api/';

  constructor(private http: HttpClient) {}

  getLeagues(): Observable<League[]> {
    return this.http.get<League[]>(`${this.url}${'leagues/'}`);
  }

  getLeague(id: number): Observable<League> {
    return this.http.get<League>(`${this.url}${'leagues/'}${id}${'/'}`)
  }

  getTeams(): Observable<Team[]> {
    return this.http.get<Team[]>(`${this.url}${'teams/'}`)
  }

  getTeamsInLeague(id: number): Observable<Team[]> {
    return this.http.get<Team[]>(`${this.url}${'leagues/'}${id}/teams/`);
  }

  private apiUrlUser = 'http://127.0.0.1:8000/users/user/';



  signUpUser(user: User): Observable<User> {
    return this.http.post<User>(this.apiUrlUser, user);
  }

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.apiUrlUser);
  }
}
