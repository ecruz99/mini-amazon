from flask import current_app as app


class Product:
    def __init__(self, id, name, link, price, category, available):
        self.id = id
        self.name = name
        self.link = link
        self.price = price
        self.category = category
        self.available = available

    @staticmethod
    def get(id):
        rows = app.db.execute('''
SELECT id, name, link, price, available
FROM Products
WHERE id = :id
''',
                              id=id)
        return Product(*(rows[0])) if rows is not None else None

    @staticmethod
    def get_all(available=True):
        rows = app.db.execute('''
SELECT id, name, link, price, category, available
FROM Products
WHERE available = :available
''',
                              available=available)
        return [Product(*row) for row in rows]

    @staticmethod
    def get_top_k(k):
        rows = app.db.execute('''
SELECT id, name, link, price, category, available
FROM Products
ORDER BY price DESC
LIMIT :k
''',
                              k=k)
        return [Product(*row) for row in rows]

    @staticmethod
    def get_by_cat(cat):
        rows = app.db.execute('''
SELECT id, name, link, price, category, available
FROM Products
WHERE category = :cat
''',
                              cat=cat)
        return [Product(*row) for row in rows]

    @staticmethod
    def get_by_kw(kw):
        rows = app.db.execute('''
SELECT id, name, link, price, category, available
FROM Products
WHERE name LIKE Concat('%', :kw, '%')
''',
                              kw=kw)
        return [Product(*row) for row in rows]