import os
import uuid
from flask import Flask, g
from vccweb.database import db_session
from vccweb.routes import auth, vcc
from typing import Optional


def create_app(database_url: str, shared_password: str) -> Flask:
    app = Flask(__name__, static_url_path="/static")
    app.secret_key = uuid.uuid4().hex
    app.config["SHARED_PASSWORD"] = shared_password
    app.config["SESSION_COOKIE_PATH"] = "/"

    @app.before_request
    def create_session():
        g.db = db_session(database_url)()

    @app.teardown_request
    def remove_session(exception=None):
        db = g.pop("db", None)
        if db is not None:
            if exception:
                db.rollback()
            else:
                db.commit()
            db.close()

    app.register_blueprint(auth)
    app.register_blueprint(vcc)

    return app


