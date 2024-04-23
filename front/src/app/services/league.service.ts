import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { League } from '../interfaces/league';

@Injectable({
  providedIn: 'root'
})
export class LeagueService {
  private url = 'http://127.0.0.1:8000/api/leagues/';

  constructor(private http: HttpClient) {}

  getLeagues(): Observable<League[]> {
    return this.http.get<League[]>(this.url);
  }

  getLeague(id: number): Observable<League> {
    return this.http.get<League>(`${this.url}${id}${'/'}`)
  }

  getTeams(): Observable<Team[]> {
    
  }
}
