import { Routes } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';
import { AboutPageComponent } from './about-page/about-page.component';
import { TeamListComponent } from './team-list/team-list.component';
import { LeagueDetailsComponent } from './league-details/league-details.component';

export const routes: Routes = [
    {path: '', redirectTo: '/home', pathMatch: 'full'},
    {path: 'home', component: HomePageComponent, title: "Home"},
    {path: 'about', component: AboutPageComponent},
    {path: 'teams', component: TeamListComponent},
    {path: 'home/league_details/:id', component: LeagueDetailsComponent}
];
