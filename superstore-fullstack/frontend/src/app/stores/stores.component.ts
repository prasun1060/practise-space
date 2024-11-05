import { Component } from '@angular/core';
import { NgFor } from '@angular/common';

import { StoreComponent } from './store/store.component';
import { type StoreModel } from './store/store.model';
import { StoresService } from './stores.service';

@Component({
  selector: 'app-stores',
  standalone: true,
  imports: [NgFor, StoreComponent],
  templateUrl: './stores.component.html',
  styleUrl: './stores.component.css'
})
export class StoresComponent {

  constructor(private storesService: StoresService) {}

  get stores() {
    return this.storesService.getAllStores()
  }

}
