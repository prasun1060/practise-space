import { NgFor } from '@angular/common';
import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-item',
  standalone: true,
  imports: [],
  templateUrl: './item.component.html',
  styleUrl: './item.component.css'
})
export class ItemComponent {

  @Input({required: true}) public item!: {id: number, name: string, price: number};
  @Output() public selectedItemForCart = new EventEmitter<{id: number, name: string, price: number}>()

  public onAddToCart () {
    console.log(`Item with id ${this.item.id} added to cart!`);
    this.selectedItemForCart.emit(this.item);
  }

}
