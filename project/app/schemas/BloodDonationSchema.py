from marshmallow import (
    Schema,
    fields,
    validate,
)


class BloodDonationSchema(Schema):
    teacher_name = fields.String(
        validate=validate.Length(min=1, max=25),
        required=True,
        error_messages={"required": "Name field cannot be empty."},
    )
    student_name = fields.String(
        validate=validate.Length(min=1, max=25),
        required=True,
        error_messages={"required": "Name field cannot be empty."},
    )
