from app.datamanager.database_manager import Database_manager
from app.models.user_model import User


class Asset:
    collection = "assets"

    def __init__(self, symbol, amount, avarage_price):
        self.symbol = symbol
        self.amount = amount
        self.avarage_price = avarage_price

    def saveAsset(self, emailAddress):
        existing_assets = self.findAssets(emailAddress)
        if not existing_assets:
            asset = {
                "userID": User.findUser(emailAddress)["_id"],
                "symbol": self.symbol,
                "amount": self.amount,
                "avarage_price": self.avarage_price
            }
        else:
            update_amount = int(existing_assets['amount']) + int(self.amount)
            find_col = {
                "name": "userID",
                "value": User.findUser(emailAddress)["_id"]
            }
            set_col = {
                "name": "amount",
                "value": update_amount
            }
            return print(Database_manager().update_one(find_col,
                         set_col, self.collection))
        Database_manager().save_one(asset, self.collection)

    @staticmethod
    def findAssets(emailAddress):
        user = User.findUser(emailAddress)
        asset = {
            "userID": user['_id']
        }
        collection = "assets"
        return Database_manager().find_one(asset, collection)
