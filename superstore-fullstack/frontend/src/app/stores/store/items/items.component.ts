import { Component } from '@angular/core';
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

  public items: { id: number, name: string, price: number }[] = [
    {
      id: 1,
      name: "Item 1",
      price: 30.0
    },
    {
      id: 2,
      name: "Item 2",
      price: 30.0
    },
    {
      id: 3,
      name: "Item 3",
      price: 30.0
    }
  ]

  item = this.items[0]

  public onAddToCart (item: { id: number, name: string, price: number }) {
    console.log(`Item with id ${item.id} added to cart!`);
  }

}
