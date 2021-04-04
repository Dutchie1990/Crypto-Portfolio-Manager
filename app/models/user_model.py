from app.datamanager.database_manager import Database_manager


class User():

    def __init__(self, emailAdress, password):
        self.emailAdress = emailAdress
        self.password = password
        self.collection = "users"

    def saveUser(self):
        register = {
            "emailaddress": self.emailAdress,
            "password": self.password
        }
        Database_manager().save_one(register, self.collection)
        return "here comes the save function"
