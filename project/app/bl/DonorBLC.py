from flask_jwt_extended import create_access_token
from project.app.repositories.DonorRepository import DonorRepository

from project.app.db import db
from flask import request, jsonify

from werkzeug.security import generate_password_hash, check_password_hash


class DonorBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def creating_donors(args):
        session = DonorBLC.get_session()
        res = DonorRepository.adding_donor(session, args)
        return res
