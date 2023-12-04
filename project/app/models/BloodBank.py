from project.app.db import db
from project.app.models.Donor import bloodBank_bloodDonation


class BloodBank(db.Model):
    __tablename__ = "bloodbank"
    BloodBankID = db.Column(db.Integer, primary_key=True)
    BloodBankName = db.Column(db.String(25))
    Location = db.Column(db.String(25))
    Email = db.Column(db.String(50), unique=True)
    ContactNumber = db.Column(db.String(50), unique=True, nullable=False)
    # AvailableBloodTypes = db.Column(db.String(25))

    blooddonations = db.relationship(
        "BloodDonation",
        secondary=bloodBank_bloodDonation,
        back_populates="bloodbanks",
    )
