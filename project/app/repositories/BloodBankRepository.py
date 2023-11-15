from project.app.models.BloodBank import BloodBank

from project.app.db import db


class BloodBankRepository:
    @staticmethod
    def get_student(id, session):
        result = session.query(BloodBank).filter(BloodBank.id == id)

        return result.first()
