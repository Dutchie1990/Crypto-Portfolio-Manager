from flask import (Blueprint, render_template, session, redirect,
                   url_for, flash, request)
from app.models.asset_model import Asset

assets = Blueprint('assets', __name__)


@assets.route('/assets', methods=["GET", "POST"])
def asset():
    if not ("username" in session):
        flash("You need to login first", "error")
        return redirect(url_for('users.login'))
    return render_template('assets.html', user=session['username'])


@assets.route('/deposit', methods=["POST"])
def deposit():
    if not ("username" in session):
        flash("You need to login first", "error")
        return redirect(url_for('users.login'))
    if request.method == "POST":
        asset = Asset("USD", request.form.get('amount'), "-")
        asset.saveAsset(session['emailaddress'])
    return redirect(url_for('assets.asset'))
