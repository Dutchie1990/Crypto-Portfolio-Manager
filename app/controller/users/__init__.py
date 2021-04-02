from flask import Blueprint

users = Blueprint('users', __name__)


@users.route('/login', methods=["GET", "POST"])
def login():
    return "Here comes the login page"


@users.route('/register', methods=["GET", "POST"])
def register():
    return "Here comes the register page"
