import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NgFor, NgIf } from '@angular/common';

import { NavbarComponent } from './navbar/navbar.component';
import { StoresComponent } from './stores/stores.component';
import { UserloginComponent } from './userlogin/userlogin.component';
import { UserregisterComponent } from './userregister/userregister.component';
import { CartComponent } from './cart/cart.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, NgFor, NgIf, NavbarComponent, StoresComponent, UserloginComponent, UserregisterComponent, CartComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';

  isUserLoggedIn: boolean = false;
  loggedInUserId?: number

  userCartItems: { id: number, name: string, price: number }[] = []

}
