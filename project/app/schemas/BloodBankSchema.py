from marshmallow import (
    Schema,
    fields,
    validate,
)


class BloodBankSchema(Schema):
    name = fields.String(
        validate=validate.Length(min=2, max=25),
        required=True,
        error_messages={"required": "Name field cannot be empty."},
    )
