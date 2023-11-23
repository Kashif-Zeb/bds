from project.app.db import db
from project.app.models.Donor import (
    donor_bloodDonation,
    bloodBank_bloodDonation,
    staff_bloodDonation,
)


class BloodDonation(db.Model):
    __tablename__ = "blooddonation"
    DonationID = db.Column(db.Integer, primary_key=True)
    DonationDate = db.Column(db.Date)
    BloodType = db.Column(db.String(25))
    DonationStatus = db.Column(db.String(50), nullable=False)
    HemoglobinLevel = db.Column(db.String(25))
    donors = db.relationship(
        "Donor",
        secondary=donor_bloodDonation,
        back_populates="blooddonations",
    )
    bloodbanks = db.relationship(
        "BloodBank",
        secondary=bloodBank_bloodDonation,
        back_populates="blooddonations",
    )
    staffs = db.relationship(
        "Staff",
        secondary=staff_bloodDonation,
        back_populates="blooddonations",
    )
