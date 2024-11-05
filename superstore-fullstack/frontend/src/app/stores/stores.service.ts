import { Injectable } from "@angular/core";
import { type StoreModel } from "./store/store.model";

@Injectable({
    providedIn: 'root'
})
export class StoresService {

    private stores: StoreModel[] = [
        {
            id: 1,
            name: 'Store 1',
            items: [
                {
                    id: 1,
                    name: 'Item 1',
                    price: 30.0
                },
                {
                    id: 2,
                    name: 'Item 2',
                    price: 60.0
                }
            ]
        },
        {
            id: 2,
            name: 'Store 2',
            items: [
                {
                    id: 3,
                    name: 'Item 3',
                    price: 30.0
                },
                {
                    id: 4,
                    name: 'Item 4',
                    price: 60.0
                }
            ]
        }
    ]

    getAllStores() {
        return this.stores;
    }

    getStore(storeId: number) {
        return this.stores.filter((store) => {store.id === storeId})[0]
    }

    getTaskFromStore(storeId: number) {
        return this.getStore(storeId).items
    }
}