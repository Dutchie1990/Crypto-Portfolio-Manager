from flask import Blueprint, render_template

users = Blueprint('users', __name__)


@users.route('/login', methods=["GET", "POST"])
def login():
    return "Here comes the login page"


@users.route('/register', methods=["GET", "POST"])
def register():
    return render_template('register.html')
