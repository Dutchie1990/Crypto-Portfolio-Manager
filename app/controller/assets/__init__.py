from flask import Blueprint

assets = Blueprint('assets', __name__)


@assets.route('/assets', methods=["GET", "POST"])
def asset():
    return "Here comes the assets page"
