from project.app.db import db

from project.app.models.Donor import staff_bloodDonation, staff_registeration


class Staff(db.Model):
    __tablename__ = "staff"
    StaffID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(25), nullable=False)
    LastName = db.Column(db.String(25), nullable=False)
    Email = db.Column(db.String(50), unique=True)
    ContactNumber = db.Column(db.String(50), unique=True, nullable=False)
    Position = db.Column(db.String(25), nullable=False)

    blooddonations = db.relationship(
        "BloodDonation",
        secondary=staff_bloodDonation,
        back_populates="staffs",
    )

    registerations = db.relationship(
        "Registeration",
        secondary=staff_registeration,
        back_populates="staffs",
    )
