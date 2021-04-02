from flask import Blueprint

transactions = Blueprint('transactions', __name__)


@transactions.route('/transactions', methods=["GET", "POST"])
def index():
    return "Here comes the transactions page"
