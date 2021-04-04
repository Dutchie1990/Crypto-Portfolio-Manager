from flask import (Blueprint, render_template,
                   request, flash)
from app.helpers.password_helper import PasswordHelper
from app.models.user_model import User

users = Blueprint('users', __name__)


@users.route('/login', methods=["GET", "POST"])
def login():
    return "Here comes the login page"


@users.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(request.form.get("email").lower(),
                    PasswordHelper().
                    generateHash(request.form.get("password")))
        result = user.saveUser()
        if (result):
            print(result)
            flash('Welcome {}'.format(
                user.emailAdress), 'success')
            return render_template('welcomescreen.html', user=user)
        else:
            print(result)
            flash("User already exist. Please proceed to login", 'error')
    return render_template('register.html')
