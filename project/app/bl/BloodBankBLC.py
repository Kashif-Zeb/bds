from project.app.repositories.BloodBankRepository import BloodBankRepository

from project.app.db import db
from flask import request, jsonify


class BloodBankBLC:
    @staticmethod
    def get_session():
        return db.session
