import pymongo
import os
if os.path.exists("env.py"):
    import env


class Database_manager:
    def __init__(self):
        self.mongo_uri = os.environ.get("MONGO_URI")
        self.db_name = os.environ.get("MONGO_DBNAME")

    def save_one(self, new_object, collection):
        db = self.connect(self, collection)

        if (collection == "users"):
            existing_user = db.find_one(
                {"emailaddress": new_object['emailaddress']})
            if existing_user:
                return False
        db.insert_one(new_object)
        return True

    def find_one(self, find_object, collection):
        db = self.connect(self, collection)

        if (collection == "users"):
            existing_user = db.find_one(
                {"emailaddress": find_object['emailaddress']})
            if existing_user:
                return existing_user

        if (collection == "assets"):
            existing_asset = db.find_one(
                {"userID": find_object['userID']})
            if existing_asset:
                return existing_asset
        return False

    def update_one(self, find_col, set_col, collection):
        db = self.connect(self, collection)
        filter = {find_col['name']: find_col['value']}
        newvalues = {"$set": {set_col['name']: set_col['value']}}
        return db.update_one(filter, newvalues)

    @staticmethod
    def connect(self, collection):
        client = pymongo.MongoClient(self.mongo_uri)
        db = client[self.db_name][collection]
        return db
