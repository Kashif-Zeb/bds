from datetime import timedelta
from http import HTTPStatus
from project.app.repositories.StaffRepository import StaffRepository

from project.app.db import db
from flask import app, current_app, request, jsonify, send_from_directory
from werkzeug.security import check_password_hash
import os
from flask_jwt_extended import create_access_token


class StaffBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def adding_staff(args, user):
        session = StaffBLC.get_session()
        # breakpoint()
        usercheck = StaffRepository.get_registeration_by_email_for_api(user, session)
        staf = [i.Position for i in usercheck.staffs]
        access = [
            "chairman",
            "director",
            "doctor",
            "nurse",
            "ceo",
        ]
        for position in staf:
            if position in access:
                res = StaffRepository.creating_staff(args, session)
                return res
            else:
                raise Exception("You don't have permission to add staff")

    @staticmethod
    def geting_single_staff(args):
        session = StaffBLC.get_session()
        res = StaffRepository.get_single_staff_id(args, session)
        return res

    @staticmethod
    def geting_all_staff():
        session = StaffBLC.get_session()
        res = StaffRepository.getting_all_staffs(session)
        return res

    @staticmethod
    def updating_staff(args):
        session = StaffBLC.get_session()
        staff = StaffRepository.get_single_staff_id(args, session)
        if staff:
            res = StaffRepository.updating_the_staff(args, session, staff)
            return res

    @staticmethod
    def deleting_staff(args):
        session = StaffBLC.get_session()
        staff = StaffRepository.get_single_staff_id(args, session)
        if not staff:
            return (
                jsonify({"message": "staff not found"}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        else:
            session.delete(staff)
            session.commit()

            return (
                jsonify({"message": f"staffid {args.get('StaffID')} is deleted"}),
                HTTPStatus.OK,
            )

    @staticmethod
    def registerating(args):
        session = StaffBLC.get_session()
        staff = StaffRepository.get_single_staff_byname(args, session)
        if staff:
            StaffRepository.registerated(args, session, staff)
        else:
            return jsonify({"message": "first provide your staff info "})

    @staticmethod
    def loggingIn(args):
        session = StaffBLC.get_session()
        email = StaffRepository.get_registeration_by_email(args, session)
        if email is not None and email.Password == args.get("Password"):
            token = create_access_token(identity=args.get("Email"))

        return token
