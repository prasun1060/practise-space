import { Component, Input } from '@angular/core';
import { ItemComponent } from './item/item.component';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-items',
  standalone: true,
  imports: [NgFor, ItemComponent],
  templateUrl: './items.component.html',
  styleUrl: './items.component.css'
})
export class ItemsComponent {

  @Input({required: true}) items!: { id: number, name: string, price: number }[]

  public onAddToCart (item: { id: number, name: string, price: number }) {
    console.log(`Item with id ${item.id} added to cart!`);
  }

}
