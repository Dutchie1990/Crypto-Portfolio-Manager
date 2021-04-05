from flask import Blueprint, flash, redirect, render_template, url_for, session

transactions = Blueprint('transactions', __name__)


@transactions.route('/transactions', methods=["GET", "POST"])
def transaction():
    print(session)
    if not ("username" in session):
        flash("You need to login first", "error")
        return redirect(url_for('users.login'))
    return render_template('welcomescreen.html', user=session['username'])
