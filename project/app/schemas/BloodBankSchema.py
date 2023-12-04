from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
)
from project.app.schemas.BloodDonationSchema import BloodDonationSchema


class BloodBankSchema(Schema):
    BloodBankID = fields.Integer(dump_only=True)
    BloodBankName = fields.String(
        validate=validate.Length(min=2, max=50),
        required=True,
    )
    Location = fields.String(
        validate=validate.Length(min=2, max=50),
        required=True,
    )
    Email = fields.Email(required=True)
    ContactNumber = fields.String(validate=validate.Length(11))

    @validates("ContactNumber")
    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) != 11:
            raise ValidationError(
                "Phone number must contain 10 digits and no other characters."
            )


class BB_BD(BloodBankSchema):
    blooddonations = fields.Nested(
        BloodDonationSchema, many=True, include=("BloodType")
    )


class update_bloodbank(BloodBankSchema):
    BloodBankID = fields.Integer(required=True)


class nested_to_Available_blood(Schema):
    Type = fields.String()
    TotalAvailable = fields.Integer()


class Available_blood(BloodBankSchema):
    BloodType = fields.Nested(nested_to_Available_blood, many=True)
