import datetime
from project.app.db import db


donor_bloodDonation = db.Table(
    "donor_bloodDonation",
    db.Column("donor_id", db.Integer, db.ForeignKey("donor.DonorID"), primary_key=True),
    db.Column(
        "bloodDonation_id",
        db.Integer,
        db.ForeignKey("blooddonation.DonationID"),
        primary_key=True,
    ),
)


# db.Column("teacher_id", db.Integer, db.ForeignKey("teacher.id"), primary_key=True),
bloodBank_bloodDonation = db.Table(
    "bloodBank_bloodDonation",
    db.Column(
        "bloodBank_id",
        db.Integer,
        db.ForeignKey("bloodbank.BloodBankID"),
        primary_key=True,
    ),
    db.Column(
        "bloodDonation_id",
        db.Integer,
        db.ForeignKey("blooddonation.DonationID"),
        primary_key=True,
    ),
)


staff_bloodDonation = db.Table(
    "staff_bloodDonation",
    db.Column("staff_id", db.Integer, db.ForeignKey("staff.StaffID"), primary_key=True),
    db.Column(
        "bloodDonation_id",
        db.Integer,
        db.ForeignKey("blooddonation.DonationID"),
        primary_key=True,
    ),
)
staff_registeration = db.Table(
    "staff_registeration",
    db.Column("staff_id", db.Integer, db.ForeignKey("staff.StaffID"), primary_key=True),
    db.Column(
        "reg_id",
        db.Integer,
        db.ForeignKey("registeration.Reg_ID"),
        primary_key=True,
    ),
)


class Donor(db.Model):
    __tablename__ = "donor"
    DonorID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(25))
    LastName = db.Column(db.String(50))
    Address = db.Column(db.String(50))
    BloodType = db.Column(db.String(50))
    Gender = db.Column(db.String(50))
    DateOfBirth = db.Column(db.Date)
    Email = db.Column(db.String(50), unique=True)
    ContactNumber = db.Column(db.String(50), unique=True, nullable=False)

    blooddonations = db.relationship(
        "BloodDonation",
        secondary=donor_bloodDonation,
        back_populates="donors",
    )
