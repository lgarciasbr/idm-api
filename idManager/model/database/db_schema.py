from marshmallow import ValidationError, Schema, fields


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')


class GroupSchema(Schema):
    id = fields.Int(dump_only=True, dump_to='_id')
    name = fields.String(required=True, validate=must_not_be_blank)


class AccountSchema(Schema):
    id = fields.Int(dump_only=True, dump_to='_id')
    password = fields.String(required=True, validate=must_not_be_blank)
    # new_password is used at change_password api method
    new_password = fields.String(required=True, validate=must_not_be_blank)
    email = fields.Email(required=True)
    url = fields.Url(dump_only=True, dump_to='_url')
    created_at = fields.DateTime(dump_only=True, dump_to='_created_at')


class TokenSchema(Schema):
    token = fields.String(required=True, validate=must_not_be_blank, dump_to='_token')
    last_accessed_date = fields.DateTime(dump_only=True, dump_to='_last_accessed_date')
