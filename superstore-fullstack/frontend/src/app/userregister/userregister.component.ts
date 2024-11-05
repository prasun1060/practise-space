import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-userregister',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './userregister.component.html',
  styleUrl: './userregister.component.css'
})
export class UserregisterComponent {

  userId: string = ""
  userName: string = ""
  userPassword: string = ""
  userEmail: string = ""

  onUserRegister() {
    console.log(this.userId, this.userName)
  }

}
