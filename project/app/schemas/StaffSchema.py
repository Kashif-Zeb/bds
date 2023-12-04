from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
)


class StaffSchema(Schema):
    StaffID = fields.Integer()
    FirstName = fields.String(
        validate=validate.Length(min=3, max=25),
        required=True,
    )
    LastName = fields.String(
        validate=validate.Length(min=3, max=25),
        required=True,
    )
    Email = fields.Email(required=True)
    Position = fields.String(
        validate=validate.Length(min=3, max=25),
        required=True,
    )
    ContactNumber = fields.String(
        validate=validate.Length(11),
        required=True,
    )

    @validates
    def validates_ContactNumber(self, value):
        if not value.isdigit() or len(value) != 11:
            raise ValidationError(
                "Phone number must contain 10 digits and no other characters."
            )


class update_schema_staff(StaffSchema):
    StaffID = fields.Integer(required=True)


class RegisterationSchema(Schema):
    Username = fields.String(required=True)
    Email = fields.Email(required=True)
    Password = fields.String(required=True)


class Login(Schema):
    Email = fields.Email(required=True)
    Password = fields.String(required=True)
