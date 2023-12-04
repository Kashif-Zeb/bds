from datetime import timedelta
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from project.app.db import db
from project.blueprints.donor import bp as donor
from project.blueprints.blood_donation import bp as blood_donation
from project.blueprints.bloodbank import bp as blood_bank
from project.blueprints.staff import bp as staff
from project import config
import os


def create_app():
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testing.db"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql+pymysql://{config.DB_USER}:{config.DB_PWD}@{config.DB_URL}:{config.DB_PORT}/{config.DB_NAME}"
    # app.config[
    #     "SQLALCHEMY_DATABASE_URI"
    # ] = "mysql+pymysql://root:kashif@localhost:3306/sms"

    db.init_app(app)
    app.config[
        "JWT_SECRET_KEY"
    ] = "60b8b427938bc9f2fbe65d98640e831b4a8522f56150b97f141677d02570819b"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
    UPLOAD_FOLDER = "uploads"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    jwt = JWTManager(app)

    @app.errorhandler(422)
    def webargs_error_handler(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        if headers:
            return jsonify({"errors": messages}), err.code, headers
        else:
            return jsonify({"errors": messages}), err.code

    # with app.app_context():
    #     db.create_all()
    app.register_blueprint(donor)
    app.register_blueprint(blood_donation)
    app.register_blueprint(blood_bank)
    app.register_blueprint(staff)
    # app.register_blueprint(teacher)
    return app
