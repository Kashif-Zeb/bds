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

from flask import Blueprint, current_app

from project.app.db import db

from marshmallow import fields, validate
from project.app.bl.DonorBLC import DonorBLC
from werkzeug.utils import secure_filename
from project.app.schemas.DonorSchema import DonorSchema


bp = Blueprint("donor", __name__)


@bp.route("/api/donors", methods=["POST"])
@use_args(DonorSchema, location="json")
def create_donor(args):
    """Create a new donor"""
    res = DonorBLC.creating_donors(args)
    std = DonorSchema(many=False)
    return std.dump(res)
