from flask import Blueprint, render_template

general = Blueprint('general', __name__)


@general.route('/')
def index():
    return render_template('welcomescreen.html')
