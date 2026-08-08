import uuid
from flask import (
    Blueprint,
    current_app,
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
)


def create_app(input_data, shared_password):
    app = Flask(__name__, static_url_path="/static")
    app.secret_key = uuid.uuid4().hex
    app.config["SHARED_PASSWORD"] = shared_password
    app.config["SESSION_COOKIE_PATH"] = "/"
    app.config["DATA"] = input_data

    app.register_blueprint(vcc_bp)

    return app


vcc_bp = Blueprint("vcc", __name__)


@vcc_bp.before_request
def require_login():
    # If already authenticated, continue
    if session.get("authenticated"):
        return

    # Endpoint unknown for static files and bad requests
    if request.endpoint is None:
        return

    # Endpoints allowed without auth
    exempt_endpoints = {"vcc.login", "static"}
    if request.endpoint in exempt_endpoints:
        return

    # Prevent redirect loop: don't redirect /login?next=/login
    if request.path.startswith(url_for("vcc.login")):
        return

    # Redirect to login page with original path as `next`
    return redirect(url_for("vcc.login", next=request.path))


@vcc_bp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    next_url = request.args.get("next") or url_for("samples.index")

    if request.method == "POST":
        if request.form.get("password") == current_app.config["SHARED_PASSWORD"]:
            session["authenticated"] = True
            return redirect(next_url)
        error = "Incorrect password"

    return render_template("login.html", error=error)


@vcc_bp.route("/logout")
def logout():
    session.pop("authenticated", None)
    return redirect(url_for("vcc.login"))


@vcc_bp.route("/")
def index():
    return render_template("index.html")


@vcc_bp.route("/samples")
def samples():
    data = current_app.config["DATA"]
    return render_template("samples.html", data=data)


