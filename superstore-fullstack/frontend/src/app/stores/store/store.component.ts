import { Component } from '@angular/core';
import { ItemsComponent } from './items/items.component';

@Component({
  selector: 'app-store',
  standalone: true,
  imports: [ItemsComponent],
  templateUrl: './store.component.html',
  styleUrl: './store.component.css'
})
export class StoreComponent {

}
