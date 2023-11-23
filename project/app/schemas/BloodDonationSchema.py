from marshmallow import (
    Schema,
    fields,
    validate,
)
from project.app.schemas.DonorSchema import DonorSchema


class BloodDonationSchema(Schema):
    DonationID = fields.Integer()
    DonationDate = fields.Date(format="%Y-%m-%d", required=True)
    BloodType = fields.String(
        validate=validate.OneOf(
            ["O+", "A+", "B+", "AB+", "O-", "A-", "B-", "AB-"],
        )
    )
    DonationStatus = fields.String(dump_only=True)
    HemoglobinLevel = fields.String(
        validate=validate.Length(min=1, max=25),
        required=True,
    )
    DonorID = fields.Integer(required=True)


class schema_to_get_BD_donor(BloodDonationSchema):
    donors = fields.Nested(DonorSchema, exclude=("DonorID", "BloodType"), many=True)


class schema_for_update_BD(Schema):
    DonationID = fields.Integer(required=True)
    DonationDate = fields.Date(format="%Y-%m-%d", required=True)
    BloodType = fields.String(
        validate=validate.OneOf(
            ["O+", "A+", "B+", "AB+", "O-", "A-", "B-", "AB-"],
        )
    )
    DonationStatus = fields.String(dump_only=True)
    HemoglobinLevel = fields.String(
        validate=validate.Length(min=1, max=25),
        required=True,
    )
    DonorID = fields.Integer(dump_only=True)
    donors = fields.Nested(DonorSchema, exclude=("DonorID", "BloodType"), many=True)


# class BloodDonationDumpSchema(BloodDonationSchema):
#     DonorID = fields.Integer(attribute="donors.DonorID", dump_only=True)


# class BloodDonationLoadSchema(BloodDonationSchema):
#     DonorID = fields.Integer(required=True)
