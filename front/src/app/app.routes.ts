import { Routes } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';
import { AboutPageComponent } from './about-page/about-page.component';
import { LeagueDetailsComponent } from './league-details/league-details.component';
import { TeamDetailsComponent } from './team-details/team-details.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { SignInComponent } from './sign-in/sign-in.component';

export const routes: Routes = [
    {path: '', redirectTo: '/home', pathMatch: 'full'},
    {path: 'home', component: HomePageComponent, title: "Home"},
    {path: 'about', component: AboutPageComponent},
    {path: 'home/league_details/:id', component: LeagueDetailsComponent},
    {path: 'home/league_details/:id/team_details/:id', component: TeamDetailsComponent},
    {path: 'signup', component: SignUpComponent},
    {path: 'signin', component: SignInComponent},
];
