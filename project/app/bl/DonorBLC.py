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

    @staticmethod
    def get_single_donor_info(args):
        session = DonorBLC.get_session()
        res = DonorRepository.get_single_donor_byid(args, session)
        return res

    @staticmethod
    def updating_existing_donor(args):
        session = DonorBLC.get_session()
        exist = DonorRepository.get_single_donor_byid(args, session)
        if exist:
            res = DonorRepository.update_donor_byid(exist, args, session)
            return res

    @staticmethod
    def get_all_donors():
        session = DonorBLC.get_session()
        donors = DonorRepository.get_all_donors(session)
        return donors

    @staticmethod
    def delete_a_donor(args):
        session = DonorBLC.get_session()

        DonorRepository.delete_donor_byid(args, session)

    @staticmethod
    def searching_donor(args):
        session = DonorBLC.get_session()
        result = DonorRepository.search_donors(args, session)
        return result
