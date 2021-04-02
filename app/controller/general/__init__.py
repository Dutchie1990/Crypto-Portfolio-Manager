from flask import Blueprint

general = Blueprint('general', __name__)


@general.route('/')
def index():
    return "Here comes the welcome page"
