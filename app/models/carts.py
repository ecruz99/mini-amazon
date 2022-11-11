from flask import current_app as app


class Cart:
    def __init__(self, uid, pid, sid, quantity, unit_price):
        self.uid = uid
        self.pid = pid
        self.sid = sid
        self.quantity = quantity
        self.unit_price = unit_price

    
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
    def delete_cart_item(uid, pid, sid):
        rows = app.db.execute('''
DELETE FROM Carts
WHERE uid = :uid
  AND pid = :pid
  AND sid = :sid
''', 
                              uid=uid, pid=pid, sid=sid)
        return None


