from app.datamanager.database_manager import Database_manager


class User():

    def __init__(self, firstName, emailAdress, password):
        self.firstName = firstName
        self.emailAdress = emailAdress
        self.password = password
        self.collection = "users"

    def saveUser(self):
        register = {
            "firstname": self.firstName,
            "emailaddress": self.emailAdress,
            "password": self.password
        }
        result = Database_manager().save_one(register, self.collection)
        return result
