from flask import request, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.BloodDonationSchema import (
    BloodDonationSchema,
    schema_for_update_BD,
    schema_to_get_BD_donor,
)

from flask import Blueprint
from http import HTTPStatus
from marshmallow import fields, Schema, validate
from project.app.bl.BloodDonationBLC import BloodDonationBLC

bp = Blueprint("blood_donation", __name__)


@bp.route("/api/add_blooddonation", methods=["POST"])
@use_args(BloodDonationSchema, location="json")
def add_blooddonation(args):
    """adding the blooddonation and associating with donor"""
    args["DonationStatus"] = "Pending"
    blood_D = BloodDonationBLC.creating_blooddonation(args)
    if not blood_D:
        return (
            jsonify({"message": "plz provide your information using add donor api"}),
            HTTPStatus.OK,
        )
    std = BloodDonationSchema()
    result = std.dump(blood_D)
    return result, HTTPStatus.CREATED


@bp.route("/api/get_single_blooddonation", methods=["GET"])
@use_args({"DonationID": fields.Integer()}, location="query")
def get_single_bloodbank(args):
    """getting blooddonation by id"""
    # breakpoint()
    res = BloodDonationBLC.getting_blooddonation(args)
    if not res:
        return jsonify({"message": "No data found"}), HTTPStatus.NOT_FOUND
    std = schema_to_get_BD_donor(many=False)
    # breakpoint()
    result = std.dump(res)
    return result, HTTPStatus.OK


@bp.route("/api/blooddonations", methods=["GET"])
def get_all_blooddonations():
    """getting all blooddonations"""
    # breakpoint()
    res = BloodDonationBLC.getting_all_blooddonations()
    if not res:
        return jsonify({"message": "records not found"}), HTTPStatus.NOT_FOUND
    std = schema_to_get_BD_donor(many=True)
    result = std.dump(res)
    return result, HTTPStatus.OK


@bp.route("/api/update_blooddonation", methods=["PUT"])
@use_args(schema_for_update_BD, location="json")
def updating_blooddonation(args):
    """updating the blooddonation"""
    args["DonationStatus"] = "Pending"
    res = BloodDonationBLC.updating_blooddonation(args)
    if not res:
        return jsonify({"message": "No data found"}), HTTPStatus.OK
    std = schema_for_update_BD()
    result = std.dump(res)
    return result, HTTPStatus.OK


@bp.route("/api/update_donationstatus", methods=["PUT"])
@use_args(
    {
        "DonationID": fields.List(fields.Integer(), required=True),
        "DonationStatus": fields.String(
            validate=validate.OneOf(["Approved", "Rejected"]), required=True
        ),
    },
    location="json",
)
def update_donationstatus(args):
    """updating the blooddonation status"""
    if len(args.get("DonationID")) == 0:
        return (
            jsonify({"DonationID": "Enter ths IDs "}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    res = BloodDonationBLC.updating_donationstatus(args)
    return res
