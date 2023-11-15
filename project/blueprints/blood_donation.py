from flask import request, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.BloodDonationSchema import BloodDonationSchema

from flask import Blueprint

from marshmallow import fields, Schema, validate
from project.app.bl.BloodDonationBLC import BloodDonationBLC

bp = Blueprint("blood_donation", __name__)
