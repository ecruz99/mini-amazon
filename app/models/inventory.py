from flask import current_app as app


class Inventory:
    def __init__(self, sellerID, productID, productname, quantity):
        self.sellerID = sellerID
        self.productID = productID
        self.productname = productname
        self.quantity = quantity

#return inventory of an inputted seller ID
    @staticmethod
    def get_seller(sellerID):
        rows = app.db.execute('''
SELECT sellerID, productID, productname, quantity
FROM Inventory
WHERE sellerID = :sellerID
''',
                              sellerID=sellerID)
        return [Inventory(*row) for row in rows]
    
#Enter seller ID and product ID to delete a product from a sellers inventory
    @staticmethod
    def delete_inventory(sellerID, productID):
        rows = app.db.execute("""
DELETE FROM Inventory
WHERE sellerID = :sellerID and productID = :productID
""",
                              sellerID = sellerID, productID = productID)
        return None