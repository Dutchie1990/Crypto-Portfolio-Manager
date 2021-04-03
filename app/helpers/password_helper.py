from werkzeug.security import generate_password_hash


class PasswordHelper:
    def __init__(self):
        pass

    def generateHash(self, password):
        return generate_password_hash(password)
