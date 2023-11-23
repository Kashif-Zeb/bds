import datetime
import os
from flask import (
    Response,
    request,
    jsonify,
    send_file,
    send_from_directory,
    make_response,
)
from webargs.flaskparser import use_args
from project.app.repositories.DonorRepository import DonorRepository
from flask import Blueprint, current_app
from marshmallow import post_dump, pre_dump
from project.app.db import db

from marshmallow import fields, validate
from project.app.bl.DonorBLC import DonorBLC
from werkzeug.utils import secure_filename
from project.app.schemas.DonorSchema import DonorSchema
from http import HTTPStatus

bp = Blueprint("donor", __name__)


@bp.route("/api/donors", methods=["POST"])
@use_args(DonorSchema, location="json")
def create_donor(args):
    """Create a new donor"""

    res = DonorBLC.creating_donors(args)
    # res.DateOfBirth = datetime.datetime.fromisoformat(res.DateOfBirth)
    std = DonorSchema(many=False)
    ans = std.dump(res)
    return ans, HTTPStatus.CREATED


@bp.route("/api/single_donor_info", methods=["GET"])
@use_args(
    {"DonorID": fields.Integer()},
    location="query",
)
def single_donor_info(args):
    """getting the single donor information"""

    res = DonorBLC.get_single_donor_info(args)
    if not res:
        return (
            jsonify({"message": f"{args} not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    # res.DateOfBirth = datetime.datetime.fromisoformat(res.DateOfBirth)
    std = DonorSchema()
    single = std.dump(res)
    return single


@bp.route("/api/update_donor_info", methods=["PUT"])
@use_args(DonorSchema, location="json")
def update_donor_info(args):
    """Update an existing donor info"""
    res = DonorBLC.updating_existing_donor(args)
    if not res:
        return (
            jsonify({"message": f"{args['DonorID']} not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    std = DonorSchema()
    updated = std.dump(res)
    return updated


@bp.route("/api/get_all_donors", methods=["GET"])
def get_all_donors():
    """getting all donors"""
    # breakpoint()
    res = DonorBLC.get_all_donors()
    std = DonorSchema(many=True)
    ans = std.dump(res)
    return ans


@bp.route("/api/delete_donors", methods=["DELETE"])
@use_args({"DonorID": fields.Integer()}, location="query")
def delete_donors(args):
    """deleting a donor from database"""
    try:
        res = DonorRepository.delete_donor_byid(args)
        return (
            jsonify({"message": f"{args['DonorID']} is deleted successfully"}),
            HTTPStatus.OK,
        )
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY
