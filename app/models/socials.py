from flask import current_app as app, flash
import datetime


class PReview:
    def __init__(self, uid, pid, rating, time_purchased):
        self.uid = uid
        self.pid = pid
        self.rating = rating
        self.time_purchased = time_purchased
        
    @staticmethod
    def getUserProductReviews(uid):
        rows = app.db.execute('''
SELECT uid, pid, rating, time_purchased
FROM P_Reviews
WHERE uid = :uid
ORDER BY time_purchased DESC
''',
                              uid=uid)
        return [PReview(*row) for row in rows]
    
    @staticmethod
    def getAProductReviews(pid):
        rows = app.db.execute('''
WITH truncated AS (
    SELECT p.uid, u.firstname, p.pid, p.rating, p.time_purchased
    FROM P_Reviews p, Users u
    WHERE p.uid = u.id)
SELECT uid, firstname, rating, time_purchased
FROM truncated
WHERE pid = :pid
ORDER BY time_purchased DESC
''',
                              pid=pid)
        return [PReview(*row) for row in rows]    

 
    
    @staticmethod
    def updateProductReview(uid, pid, rating):
        rows = app.db.execute('''
UPDATE P_Reviews
SET rating = :rating
WHERE uid = :uid and pid = :pid
''',
                              uid=uid, pid = pid, rating = rating)
        return None
    
    @staticmethod
    def createProductReview(uid, pid, rating):
        currentdate = datetime.datetime.now()
        try:
            rows = app.db.execute('''
INSERT INTO P_Reviews(uid, pid, rating, time_purchased)
VALUES(:uid, :pid, :rating, :time_purchased)
''',
                              uid=uid, pid = pid, rating = rating, time_purchased = currentdate)
            return None   
    
        except Exception as e:
            # likely email already in use; better error checking and reporting needed;
            # the following simply prints the error to the console:
            print(str(e))
            return None 

    @staticmethod
    def reviewexist(uid, pid):
        rows = app.db.execute("""
SELECT uid, pid
FROM P_Reviews
WHERE pid = :pid and uid = :uid
""",
                              uid = uid, pid = pid)
        return len(rows) > 0

    @staticmethod
    def deletereview(uid, pid):
        rows = app.db.execute("""
DELETE FROM P_Reviews
WHERE uid = :uid and pid = :pid
""",
                              uid = uid, pid = pid)
        return None
    
    @staticmethod
    def getAverage(pid):
        rows = app.db.execute('''
SELECT AVG(rating)
FROM P_Reviews
WHERE pid = :pid
''',
                              pid=pid)
        return int(rows[0][0]) 
