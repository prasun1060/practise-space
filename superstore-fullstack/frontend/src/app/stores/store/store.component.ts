import { Component, Input } from '@angular/core';
import { ItemsComponent } from './items/items.component';

@Component({
  selector: 'app-store',
  standalone: true,
  imports: [ItemsComponent],
  templateUrl: './store.component.html',
  styleUrl: './store.component.css'
})
export class StoreComponent {

  @Input({required: true}) store!: {id: number, name: string, items: {id: number, name: string, price: number}[]}

}
