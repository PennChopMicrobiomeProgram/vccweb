import os
import uuid
from flask import Flask, g
from vccweb.database import db_session
from vccweb.routes import vcc_bp
from typing import Optional


def create_app(input_data, shared_password):
    app = Flask(__name__, static_url_path="/static")
    app.secret_key = uuid.uuid4().hex
    app.config["SHARED_PASSWORD"] = shared_password
    app.config["SESSION_COOKIE_PATH"] = "/"
    app.config["DATA"] = input_data

    app.register_blueprint(vcc_bp)

    return app


