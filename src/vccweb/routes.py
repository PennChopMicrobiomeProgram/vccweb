from datetime import date as date_type

from flask import (
    Blueprint,
    current_app,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)


auth = Blueprint("auth", __name__)

@auth.before_request
def require_login():
    # If already authenticated, continue
    if session.get("authenticated"):
        return

    # Endpoint unknown for static files and bad requests
    if request.endpoint is None:
        return

    # Endpoints allowed without auth
    exempt_endpoints = {"auth.login", "static"}
    if request.endpoint in exempt_endpoints:
        return

    # Prevent redirect loop: don't redirect /login?next=/login
    if request.path.startswith(url_for("auth.login")):
        return

    # Redirect to login page with original path as `next`
    return redirect(url_for("auth.login", next=request.path))


@auth.route("/login", methods=["GET", "POST"])
def login():
    error = None
    next_url = request.args.get("next") or url_for("samples.index")

    if request.method == "POST":
        if request.form.get("password") == current_app.config["SHARED_PASSWORD"]:
            session["authenticated"] = True
            return redirect(next_url)
        error = "Incorrect password"

    return render_template("login.html", error=error)


@auth.route("/logout")
def logout():
    session.pop("authenticated", None)
    return redirect(url_for("auth.login"))


vcc = Blueprint("vcc", __name__)

### Pages ###
@vcc.route("/")
def index():
    return render_template("index.html")


@vcc.route("/libraries")
def samples():
    header = list(Library.__table__.columns.keys())
    list(inspect(Library).column_attrs.keys())

    attrs = list(inspect(Model).column_attrs)
    return render_template("samples.html", columns=columns, date_columns=date_columns)


### API ###
@vcc.route("/api/samples")
def samples_api():
    columns = [c.name for c in Sample.__table__.columns]
    db = g.db
    samples_data = []
    for sample in db.query(Sample).all():
        record = {}
        for col in columns:
            value = getattr(sample, col)
            if isinstance(value, date_type):
                record[col] = value.isoformat()
            else:
                record[col] = value
        samples_data.append(record)
    return jsonify({"data": samples_data})
