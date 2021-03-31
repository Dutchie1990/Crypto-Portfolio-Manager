from flask import Flask
from users import users
import os
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.register_blueprint(users)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
