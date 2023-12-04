from project.app.db import db
from project.app.models.Donor import staff_registeration


class Registeration(db.Model):
    __tablename__ = "registeration"
    Reg_ID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(50), unique=True, nullable=False)
    Email = db.Column(db.String(50), unique=True, nullable=False)
    Password = db.Column(db.String(180), nullable=False)
    staffs = db.relationship(
        "Staff",
        secondary=staff_registeration,
        back_populates="registerations",
    )
