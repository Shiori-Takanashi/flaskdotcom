from flask import Blueprint, render_template, request

from ..services.company_service import get_pagination


bp_company = Blueprint("company", __name__, url_prefix="/company-list")


@bp_company.route("/")
def company_list():
    pagination = get_pagination(
        request.args.get("requested_page", 1, type=int),
        request.args.get("per_page", 12, type=int),
    )
    return render_template("pages/company.html", pagination=pagination)
