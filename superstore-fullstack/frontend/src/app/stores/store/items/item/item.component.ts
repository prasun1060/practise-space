import { Component } from '@angular/core';

@Component({
  selector: 'app-item',
  standalone: true,
  imports: [],
  templateUrl: './item.component.html',
  styleUrl: './item.component.css'
})
export class ItemComponent {

  public item: {id: number, name: string, price: number} = {
    id: 1,
    name: "Item 1",
    price: 30.0
  }

  onAddToCart () {
    console.log(`Item with id ${this.item.id} added to cart!`)
  }

}
