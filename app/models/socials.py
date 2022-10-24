from flask import current_app as app


class PReview:
    def __init__(self, uid, pid, rating, review, time_purchased):
        self.uid = uid
        self.pid = pid
        self.rating = rating
        self.review = review
        self.time_purchased = time_purchased
        
    @staticmethod
    def getTopFive(uid):
        rows = app.db.execute('''
SELECT uid, pid, rating, review, time_purchased
FROM P_Review
WHERE uid = :uid
ORDER BY time_purchased DESC
LIMIT :5
''',
                              uid=uid)
        return [PReview(*row) for row in rows]
