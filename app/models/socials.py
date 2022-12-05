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
SELECT name, rating, review
FROM Products u, P_Reviews p
WHERE uid = :uid AND pid = id
ORDER BY time_purchased DESC
''',
                              uid=uid)
        return rows
    
    @staticmethod
    def getAProductReviews(pid):
        rows = app.db.execute('''
    SELECT CONCAT(firstname, ' ', lastname) AS name, rating, review, uid
    FROM Users u, P_Reviews p
    WHERE uid = id AND pid = :pid
    ORDER BY time_purchased DESC
''',
                              pid=pid)
        return rows    

    @staticmethod
    def numberOfReview(pid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM P_Reviews
    WHERE pid = :pid
''',
                              pid=pid)
        return int(rows[0][0]) 
    
    @staticmethod
    def updateProductReview(uid, pid, rating, review):
        rows = app.db.execute('''
UPDATE P_Reviews
SET rating = :rating, review = :review
WHERE uid = :uid and pid = :pid
''',
                              uid=uid, pid = pid, rating = rating, review = review)
        return None
    
    @staticmethod
    def createProductReview(uid, pid, rating, review, link):
        currentdate = datetime.datetime.now()
        try:
            rows = app.db.execute('''
INSERT INTO P_Reviews(uid, pid, rating, review, link, time_purchased)
VALUES(:uid, :pid, :rating, :review, :link, :time_purchased)
''',
                              uid=uid, pid = pid, rating = rating, time_purchased = currentdate, review = review, link = link)
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
        return int(rows[0][0]) if rows else None

    @staticmethod
    def numberOfReviewOne(pid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM P_Reviews
    WHERE pid = :pid AND rating = 1
''',
                              pid=pid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewTwo(pid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM P_Reviews
    WHERE pid = :pid AND rating = 2
''',
                              pid=pid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewThree(pid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM P_Reviews
    WHERE pid = :pid AND rating = 3
''',
                              pid=pid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewFour(pid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM P_Reviews
    WHERE pid = :pid AND rating = 4
''',
                              pid=pid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewFive(pid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM P_Reviews
    WHERE pid = :pid AND rating = 5
''',
                              pid=pid)
        return int(rows[0][0]) 
    
    @staticmethod
    def orderExist(uid, pid):
        rows = app.db.execute('''
    SELECT uid, pid
    FROM Orders
    WHERE pid = :pid AND uid = :uid
''',
                              pid=pid, uid = uid)
        return len(rows) > 0
    
    @staticmethod
    def getAPReviewLinks(pid):
        rows = app.db.execute('''
    SELECT link, CONCAT(firstname, ' ', lastname) AS name
    FROM Users u, P_Reviews p
    WHERE uid = id AND pid = :pid
''',
                              pid=pid)
        return rows  
    
    #########################################
    
    @staticmethod
    def getAverageU(uid):
        rows = app.db.execute('''
    SELECT AVG(rating)
    FROM P_Reviews
    WHERE uid = :uid
    ''',
                              uid=uid)
        if rows is not None:
            return int(rows[0][0])
        return None
    
    @staticmethod
    def numberOfReviewU(uid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM P_Reviews
    WHERE uid = :uid
''',
                              uid=uid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewOneU(uid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM P_Reviews
    WHERE uid = :uid AND rating = 1
''',
                              uid=uid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewTwoU(uid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM P_Reviews
    WHERE uid = :uid AND rating = 2
''',
                              uid=uid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewThreeU(uid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM P_Reviews
    WHERE uid = :uid AND rating = 3
''',
                              uid=uid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewFourU(uid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM P_Reviews
    WHERE uid = :uid AND rating = 4
''',
                              uid=uid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewFiveU(uid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM P_Reviews
    WHERE uid = :uid AND rating = 5
''',
                              uid=uid)
        return int(rows[0][0]) 
    
    ##############################################################
    
    @staticmethod
    def getAverageS(uid):
        rows = app.db.execute('''
    SELECT AVG(rating)
    FROM S_Reviews
    WHERE uid = :uid
    ''',
                              uid=uid)
        if rows is not None:
            return int(rows[0][0])
        return None
    
    @staticmethod
    def numberOfReviewS(uid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM S_Reviews
    WHERE uid = :uid
''',
                              uid=uid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewOneS(uid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM S_Reviews
    WHERE uid = :uid AND rating = 1
''',
                              uid=uid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewTwoS(uid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM S_Reviews
    WHERE uid = :uid AND rating = 2
''',
                              uid=uid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewThreeS(uid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM S_Reviews
    WHERE uid = :uid AND rating = 3
''',
                              uid=uid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewFourS(uid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM S_Reviews
    WHERE uid = :uid AND rating = 4
''',
                              uid=uid)
        return int(rows[0][0]) 
    
    @staticmethod
    def numberOfReviewFiveS(uid):
        rows = app.db.execute('''
    SELECT COUNT(*)
    FROM S_Reviews
    WHERE uid = :uid AND rating = 5
''',
                              uid=uid)
        return int(rows[0][0]) 
    
    @staticmethod
    def getSellerProductReviews(uid):
        rows = app.db.execute('''
SELECT CONCAT(firstname, ' ', lastname) AS name, rating, review
FROM Users u, S_Reviews s
WHERE sid = :uid AND uid = id
ORDER BY time_purchased DESC
''',
                              uid=uid)
        return rows
    