from werkzeug.security import generate_password_hash, check_password_hash


class PasswordHelper:

    @staticmethod
    def generateHash(password):
        return generate_password_hash(password)

    @staticmethod
    def checkPassword(input_password, db_password):
        if(check_password_hash(db_password, input_password)):
            return True
        return False
