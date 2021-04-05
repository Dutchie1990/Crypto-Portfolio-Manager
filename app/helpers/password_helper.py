from werkzeug.security import generate_password_hash


class PasswordHelper:

    @staticmethod
    def generateHash(password):
        return generate_password_hash(password)
