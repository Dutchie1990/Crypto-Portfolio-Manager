from app.datamanager.database_manager import Database_manager


class User():
    collection = "users"

    def __init__(self, firstName, emailAdress, password):
        self.firstName = firstName
        self.emailAdress = emailAdress
        self.password = password

    def saveUser(self):
        register = {
            "firstname": self.firstName,
            "emailaddress": self.emailAdress,
            "password": self.password
        }
        return Database_manager().save_one(register, self.collection)

    @staticmethod
    def findUser(emailAdress):
        user = {
            "emailaddress": emailAdress
        }
        collection = "users"
        return Database_manager().find_one(user, collection)
