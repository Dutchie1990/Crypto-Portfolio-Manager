import pymongo
import os
if os.path.exists("env.py"):
    import env


class Database_manager:
    def __init__(self):
        self.mongo_uri = os.environ.get("MONGO_URI")
        self.db_name = os.environ.get("MONGO_DBNAME")

    def save_one(self, new_object, collection, duplication):
        db = self.connect(self, collection)
        if not duplication:
            existing_user = db.find_one(
                {"emailaddress": new_object['emailaddress']})
            if existing_user:
                return print('user does exist proceed to login')
            db.insert_one(new_object)
            return print('objectsaved')

    @staticmethod
    def connect(self, collection):
        client = pymongo.MongoClient(self.mongo_uri)
        db = client[self.db_name][collection]
        return db
