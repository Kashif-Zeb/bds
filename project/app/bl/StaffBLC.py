from project.app.repositories.StaffRepository import StaffRepository

from project.app.db import db
from flask import app, current_app, request, jsonify, send_from_directory

import os


class StaffBLC:
    @staticmethod
    def get_session():
        return db.session
