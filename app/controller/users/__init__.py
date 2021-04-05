from flask import (Blueprint, render_template,
                   request, flash, Markup, session, redirect, url_for)
from app.helpers.password_helper import PasswordHelper
from app.models.user_model import User

users = Blueprint('users', __name__)


@users.route('/login', methods=["GET", "POST"])
def login():
    if ("username" in session):
        flash("You already logged in", "error")
        return render_template("welcomescreen.html", user=session['username'])
    if request.method == "POST":
        existing_user = User.findUser(request.form.get('email').lower())
        if(existing_user):
            if(PasswordHelper.checkPassword(request.form.get('password'),
                                            existing_user['password'])):
                user = User(existing_user['firstname'],
                            existing_user['emailaddress'],
                            existing_user['password'])
                flash("Welcome back {}".format(user.firstName), "success")
                session['username'] = user.firstName
                return render_template('welcomescreen.html',
                                       user=session['username'])
            else:
                flash("Username and/or password are incorrect", "error")
        else:
            flash("Username does not exist", "error")
    return render_template('login.html')


@users.route('/register', methods=["GET", "POST"])
def register():
    if ("username" in session):
        flash("You already logged in", "error")
        return render_template("welcomescreen.html", user=session['username'])
    if request.method == "POST":
        user = User(request.form.get('firstname').lower(),
                    request.form.get("email").lower(),
                    PasswordHelper.
                    generateHash(request.form.get("password")))
        result = user.saveUser()
        if (result):
            flash('Welcome {}'.format(
                user.firstName.capitalize()), 'success')
            session['username'] = user.firstName
            return render_template('welcomescreen.html',
                                   user=session['username'])
        else:
            flash(Markup(
                ''''User already exists, please <a href="/login"
                class="alert-link">login</a>'''),
                'error')
    return render_template('register.html')


@users.route("/logout")
def logout():
    flash("You have been logged out")
    session.clear()
    return redirect(url_for('users.login'))
