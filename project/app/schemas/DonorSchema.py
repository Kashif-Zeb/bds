from marshmallow import (
    Schema,
    fields,
    validate,
)

from enum import Enum


class BloodType(Enum):
    O_POSITIVE = "O+"
    A_POSITIVE = "A+"
    B_POSITIVE = "B+"
    AB_POSITIVE = "AB+"
    O_NEGATIVE = "O-"
    A_NEGATIVE = "A-"
    B_NEGATIVE = "B-"
    AB_NEGATIVE = "AB-"


class DonorSchema(Schema):
    DonorID = fields.Integer()
    FirstName = fields.String(
        validate=validate.Length(min=1),
        required=True,
    )
    LastName = fields.String(
        validate=validate.Length(min=1),
        required=True,
    )
    Address = fields.String(
        validate=validate.Length(min=1),
        required=True,
    )
    BloodType = fields.String(
        validate=validate.OneOf(["O+", "A+", "B+", "AB+", "O-", "A-", "b-", "AB-"])
    )
    Gender = fields.String(validate=validate.OneOf(["Male", "Female"]))
    DateOfBirth = fields.Date(format="%Y-%m-%d", required=True)
    Email = fields.Email(required=True)
    ContactNumber = fields.String(
        validate=validate.Length(min=10, max=11),
        required=True,
    )
