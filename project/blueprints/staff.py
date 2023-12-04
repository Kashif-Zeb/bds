from flask import request, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.StaffSchema import (
    Login,
    StaffSchema,
    update_schema_staff,
    RegisterationSchema,
)
from functools import wraps
from flask import Blueprint

from project.app.db import db
from project.app.repositories.StaffRepository import StaffRepository
from marshmallow import fields, Schema, validate
from project.app.bl.StaffBLC import StaffBLC
from http import HTTPStatus
from flask_jwt_extended import jwt_required

bp = Blueprint("staff", __name__)


def role_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = request.headers.get("Email")
        if user is None:
            raise Exception("No email authentication in the headers")

        session = db.session
        usercheck = StaffRepository.get_registeration_by_email_for_api(user, session)
        staf = [i.Position for i in usercheck.staffs]
        access = [
            "chairman",
            "director",
            "doctor",
            "nurse",
            "ceo",
        ]

        # Check if any of the user's positions allow access
        for position in staf:
            if position in access:
                # User has access, execute the decorated function
                return func(*args, **kwargs)

        # User doesn't have necessary positions
        raise Exception("not allowed to access the api")

    return wrapper


@bp.route("/api/register", methods=["POST"])
@use_args(RegisterationSchema, location="json")
def register(args):
    """registering user"""
    staffBL = StaffBLC.registerating(args)
    return {"message": "Successfully registered"}, HTTPStatus.OK


@bp.route("/api/login", methods=["POST"])
@use_args(Login, location="json")
def login(args):
    """log in"""
    staffBL = StaffBLC.loggingIn(args)

    return jsonify({"token": f"Bearer {staffBL}", "email": args.get("Email")})


@bp.route("/api/add_staff", methods=["POST"])
@jwt_required()
@use_args(StaffSchema, location="json")
def add_staff(args):
    """adding the staff"""
    try:
        user = request.headers.get("Email")
        if user is None:
            raise Exception("not email authentication in the headers")

        staff = StaffBLC.adding_staff(args, user)
        std = StaffSchema()
        result = std.dump(staff)
        return result, HTTPStatus.CREATED
    except Exception as e:
        return jsonify({"message": str(e)})


@bp.route("/api/get_single_staff", methods=["GET"])
@jwt_required()
@role_required
@use_args({"StaffID": fields.Integer()}, location="query")
def get_single_staff(args):
    """getting single staff by id"""
    staff = StaffBLC.geting_single_staff(args)
    if not staff:
        return jsonify({"message": "staff not found"}), HTTPStatus.UNPROCESSABLE_ENTITY
    std = StaffSchema()
    result = std.dump(staff)
    return result, HTTPStatus.OK


@bp.route("/api/get_all_staff", methods=["GET"])
@jwt_required()
@role_required
def get_all_staff():
    """getting all staff"""
    try:
        staff = StaffBLC.geting_all_staff()
        if not staff:
            return (
                jsonify({"message": "there is no staffs"}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        std = StaffSchema(many=True)
        result = std.dump(staff)
        return result, HTTPStatus.OK
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/api/update_staff", methods=["PUT"])
@jwt_required()
@role_required
@use_args(update_schema_staff, location="json")
def update_staff(args):
    """updating the staff"""
    staff = StaffBLC.updating_staff(args)
    if not staff:
        return jsonify({"message": "staff not found"}), HTTPStatus.UNPROCESSABLE_ENTITY
    std = update_schema_staff()
    result = std.dump(staff)
    return result, HTTPStatus.OK


@bp.route("/api/delete_staff", methods=["DELETE"])
@jwt_required()
@role_required
@use_args({"StaffID": fields.Integer()}, location="query")
def delete_staff(args):
    """deleting the staff"""
    staff = StaffBLC.deleting_staff(args)
    return staff
