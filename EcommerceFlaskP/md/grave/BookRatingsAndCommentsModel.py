from datetime import datetime

from settings import db


class ProductRatingsAndComments(db.Model):
    __tablename__ = 'productRatings'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    productId = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(500), nullable=False)
    anonymous = db.Column(db.BOOLEAN, default=False, nullable=False)
    createdDate = db.Column(db.DateTime, default=datetime.utcnow)


def add_rating_and_comment(_userId, _productId, _rating, _comments, _anonymous):
    if _anonymous == 'on':
        _anonymous = 1
        _userId = - 1
    new_rating_and_comment = ProductRatingsAndComments(userId=_userId, productId=_productId, rating=_rating, comments=_comments,
                                                    anonymous=_anonymous)
    db.session.add(new_rating_and_comment)
    db.session.commit()
