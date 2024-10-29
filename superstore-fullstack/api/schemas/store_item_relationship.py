from schemas.store import PlainStoreSchema
from schemas.item import PlainItemSchema

from marshmallow import fields

class ItemSchema(PlainItemSchema):

    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(lambda: PlainStoreSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):

    items = fields.List(fields.Nested(lambda: PlainItemSchema()), dump_only=True)