from schemas.item import PlainItemSchema
from schemas.store import PlainStoreSchema
from schemas.user import UserSchema, UserAuthenticationSchema
from schemas.store_item_relationship import ItemSchema, StoreSchema
from schemas.user_cart_item_relationship import UserCartSchema, CartItemSchema


plain_item_schema = PlainItemSchema()
plain_items_schema = PlainItemSchema(many=True)

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

plain_store_schema = PlainStoreSchema()
plain_stores_schema = PlainStoreSchema(many=True)

store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)

user_schema = UserSchema()
user_authentication_schema = UserAuthenticationSchema()
cart_item_schema = CartItemSchema()
user_cart_schema = UserCartSchema()