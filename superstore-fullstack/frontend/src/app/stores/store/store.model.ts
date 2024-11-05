import { ItemModel } from "./items/item/item.model";

export interface StoreModel {
    id: number;
    name: string;
    items: ItemModel[]
}