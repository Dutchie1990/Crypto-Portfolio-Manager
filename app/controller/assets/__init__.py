from flask import Blueprint, render_template

assets = Blueprint('assets', __name__)


@assets.route('/assets', methods=["GET", "POST"])
def asset():
    return render_template('homescreen.html', user=user)
