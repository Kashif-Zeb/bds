from flask import request, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.BloodBankSchema import (
    BloodBankSchema,
    BB_BD,
    update_bloodbank,
    Available_blood,
)

from flask import Blueprint

from project.app.db import db

from marshmallow import fields, validate
from project.app.bl.BloodBankBLC import BloodBankBLC
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    unset_jwt_cookies,
)
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus


bp = Blueprint("bloodbank", __name__)


@bp.route("/api/add_bloodbank", methods=["POST"])
@use_args(BloodBankSchema, location="json")
def add_bloodbank(args):
    """adding the bloodbank"""
    bloodbank = BloodBankBLC.adding_bloodbank(args)
    std = BloodBankSchema()
    data = std.dump(bloodbank)
    return data, HTTPStatus.CREATED


@bp.route("/api/single_bloodbank_info", methods=["GET"])
@use_args({"BloodBankID": fields.Integer()}, location="query")
def single_bloodbank_info(args):
    """getting the single bloodbank info"""
    bloodbank = BloodBankBLC.get_single_bb(args)
    if not bloodbank:
        return (
            jsonify({"message": "bloodbank not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    std = BB_BD()
    result = std.dump(bloodbank)
    return result


@bp.route("/api/update_bloodbank", methods=["PUT"])
@use_args(update_bloodbank, location="json")
def updatebloodbank(args):
    """update the bloodbank info"""
    bloodbank = BloodBankBLC.updating_bloodbank(args)
    if not bloodbank:
        return (
            jsonify({"message": "bloodbank not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    std = BB_BD()
    result = std.dump(bloodbank)
    return result, HTTPStatus.OK


@bp.route("/api/get_all_bloodbank", methods=["GET"])
def get_all_bloodbank():
    """getting all bloodbank info"""
    # breakpoint()
    bloodbank = BloodBankBLC.get_all_bb()
    if not bloodbank:
        return (
            jsonify({"message": "bloodbank not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    std = BB_BD(many=True)
    result = std.dump(bloodbank)
    return result, HTTPStatus.OK


@bp.route("/api/delete_bloodbank", methods=["DELETE"])
@use_args({"BloodBankID": fields.Integer()}, location="query")
def delete_bloodbank(args):
    """deleting a bloodbank"""
    bloodbank = BloodBankBLC.delete_bloodbank(args)
    return bloodbank, HTTPStatus.NO_CONTENT


@bp.route("/api/get_available_blood", methods=["GET"])
@use_args({"BloodBankName": fields.String()}, location="query")
def available_blood(args):
    """Getting Available Blood in a particular Blood Bank"""
    bloods = BloodBankBLC.get_availble_bloods(args)
    if not bloods:
        return (
            jsonify({"message": "bloodbank not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    std = Available_blood(many=True)
    result = std.dump(bloods)
    return result, HTTPStatus.OK


@bp.route("/api/get_all_availableblood", methods=["GET"])
def get_all_availableblood():
    """Getting All Available Blood In All Blood Banks"""
    bloods = BloodBankBLC.gets_all_availble_bloods()
    if not bloods:
        return (
            jsonify({"message": "there is not any bloodbank in db"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    std = Available_blood(many=True)
    result = std.dump(bloods)
    return result, HTTPStatus.OK
