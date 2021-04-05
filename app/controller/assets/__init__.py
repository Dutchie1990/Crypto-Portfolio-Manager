from flask import Blueprint, render_template, session, redirect, url_for, flash

assets = Blueprint('assets', __name__)


@assets.route('/assets', methods=["GET", "POST"])
def asset():
    if not ("username" in session):
        flash("You need to login first", "error")
        return redirect(url_for('users.login'))
    return render_template('welcomescreen.html', user=session['username'])
