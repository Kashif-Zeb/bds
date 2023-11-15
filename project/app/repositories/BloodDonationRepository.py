from project.app.models.BloodDonation import BloodDonation
from project.app.db import db


class BloodDonationRepository:
    @staticmethod
    def get_teacher_name(session, teacher_name):
        res = (
            session.query(BloodDonation)
            .filter(BloodDonation.name == teacher_name)
            .first()
        )
        return res
