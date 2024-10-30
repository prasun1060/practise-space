import { Component } from '@angular/core';
import { StoreComponent } from './store/store.component';

@Component({
  selector: 'app-stores',
  standalone: true,
  imports: [StoreComponent],
  templateUrl: './stores.component.html',
  styleUrl: './stores.component.css'
})
export class StoresComponent {

}
