from flask import current_app as app


class Inventory:
    def __init__(self, sellerID, productID, productname, quantity):
        self.sellerID = sellerID
        self.productID = productID
        self.productname = productname
        self.quantity = quantity


    @staticmethod
    def get_seller(sellerID):
        rows = app.db.execute('''
SELECT sellerID, productID, productname, quantity
FROM Inventory
WHERE sellerID = :sellerID
''',
                              sellerID=sellerID)
        return Inventory(*(rows[0])) if rows is not None else None