from flask import Flask
from app.controller.general import general
from app.controller.users import users
from app.controller.assets import assets
from app.controller.transactions import transactions
import os
if os.path.exists("env.py"):
    import env


app = Flask(__name__, template_folder='app/templates',
            static_folder='app/static')
app.secret_key = os.environ.get("SECRET_KEY")
app.register_blueprint(general)
app.register_blueprint(users)
app.register_blueprint(assets)
app.register_blueprint(transactions)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
