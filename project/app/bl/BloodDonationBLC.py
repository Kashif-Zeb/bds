from project.app.repositories.BloodDonationRepository import BloodDonationRepository
from project.app.db import db
from flask import request, jsonify


class BloodDonationBLC:
    @staticmethod
    def get_session():
        return db.session
