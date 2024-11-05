import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {

  @Input({required: true}) isUserLoggedIn!: Boolean;
  @Input({required: false}) noOfCartItems: number = 0;
  
}
