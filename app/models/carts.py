from flask import current_app as app


class Care:
    def __init__(self, uid, pid, sid, productname, quantity, unit_price):
        self.uid = uid
        self.pid = pid
        self.sid = sid
        self.productname = productname
        self.quantity = quantity
        self.unit_price = unit_price

    
    @staticmethod
    def get_cart(uid):
        rows = app.db.execute('''
SELECT uid, pid, sid, productname, quantity, unit_price
FROM Carts
WHERE uid = :uid
''',
                              uid=uid)
        return [Carts(*row) for row in rows]


