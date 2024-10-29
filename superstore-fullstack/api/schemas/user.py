from marshmallow import Schema, fields


class UserAuthenticationSchema(Schema):

    id = fields.Str(required=True)
    password = fields.Str(load_only=True, required=True)

class UserSchema(UserAuthenticationSchema):

    name = fields.Str(required=True)
    email_id = fields.Str(required=True)