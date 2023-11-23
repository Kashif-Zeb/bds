from flask import request, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.StaffSchema import StaffSchema

from flask import Blueprint

from project.app.db import db

from marshmallow import fields, Schema, validate
from project.app.bl.StaffBLC import StaffBLC


bp = Blueprint("staff", __name__)
