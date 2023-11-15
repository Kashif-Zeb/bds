from flask import request, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.BloodBankSchema import BloodBankSchema

from flask import Blueprint
from project.app.models.student import Student
from project.app.models.Department import Department
from project.app.models.Teacher import Teacher
from project.app.models.Course import Course
from project.app.models.Users import Users
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


bp = Blueprint("bloodbank", __name__)
