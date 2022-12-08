from flask import current_app as app

class Cart:
    def __init__(self, uid, pid, sid, quantity, unit_price):
        self.uid = uid
        self.pid = pid
        self.sid = sid
        self.quantity = quantity
        self.unit_price = unit_price

    @staticmethod
    def num_items_in_cart(uid):
        rows=app.db.execute('''
SELECT SUM(quantity)
FROM Carts
WHERE uid=:uid
''',
                              uid=uid)
        if rows:
            return 1
        else:
            return 0

    @staticmethod
    def subtotal(uid):
        rows=app.db.execute('''
SELECT SUM(unit_price*quantity)
FROM Carts
WHERE uid=:uid
''',
                              uid=uid)
        if rows:
            return 1
        else:
            return 0

    @staticmethod
    def get_cart(uid):
        rows = app.db.execute('''
SELECT uid, pid, sid, quantity, unit_price
FROM Carts
WHERE uid = :uid
''',
                              uid=uid)
        return [Cart(*row) for row in rows]
    
    @staticmethod
    def delete_cart_item(uid, pid):
        rows = app.db.execute('''
DELETE FROM Carts
WHERE uid = :uid
  AND pid = :pid
''', 
                              uid=uid, pid=pid)
        return None
        
    @staticmethod
    def insert_into_cart(uid, pid, sid, productname, quantity, unit_price):
        rows = app.db.execute('''
INSERT INTO Carts(uid, pid, sid, productname, quantity, unit_price)
Values(:uid, :pid, :sid, :productname, :quantity, :unit_price)
''',
                              uid=uid, pid=pid, sid=sid, productname=productname, quantity=quantity, unit_price=unit_price)
        return None
        
    @staticmethod
    def update_quantity(uid, pid, sid, quantity):
        rows = app.db.execute('''
UPDATE Carts
SET quantity = :quantity
WHERE uid = :uid
  AND pid = :pid
  AND sid = :sid 
''', 
                              uid=uid, pid=pid, sid=sid, quantity=quantity)
        return None


