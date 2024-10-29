from schemas import UserSchema, PlainItemSchema
from marshmallow import fields, Schema


class CartItemSchema(Schema):

    user_id = fields.Str(required=True, dump_only=True)
    item_id = fields.Int(required=True, load_only=True)
    item = fields.Nested(PlainItemSchema(), dump_only=True)
    quantity = fields.Int(required=True)

class UserCartSchema(UserSchema):

    user_id = fields.Str(required=True, load_only=True)
    cart_items = fields.List(fields.Nested(CartItemSchema()), dump_only=True)