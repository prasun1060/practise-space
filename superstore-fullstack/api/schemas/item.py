from marshmallow import Schema, fields


class PlainItemSchema(Schema):

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    
class ItemUpdateSchema(Schema):

    name = fields.Str()
    price = fields.Float()
    