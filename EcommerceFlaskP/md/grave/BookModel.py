from settings import db
import json

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(128))
    title = db.Column(db.String(128))
    description = db.Column(db.String(128))
    price = db.Column(db.Float)
    authorName = db.Column(db.String(50))
    publisher = db.Column(db.String(128))
    genre = db.Column(db.String(32))

    def get_all_products():
        return Product.query.all()


    def get_product(_productId):
        return Product.json(Product.query.filter_by(productId=_productId).first())

    def delete_product(_productId):
        is_successful = Product.query.filter_by(productId=_productId).delete()
        db.session.commit()
        return bool(is_successful)

    def update_product_price(_productId, _price):
        product_to_update = Product.query.filter_by(productId=_productId).first()
        product_to_update.price = _price
        db.session.commit()

    def update_product_name(_productId, _productTitle):
        product_to_update = Product.query.filter_by(productId=_productId).first()
        product_to_update.productTitle = _productTitle
        db.session.commit()

    def update_product_rating(_productId, _rating):
        product_to_update = Product.query.filter_by(productId=_productId).first()
        product_to_update.rating = _rating
        db.session.commit()

    def update_product_comments(_productId, _comments):
        product_to_update = Product.query.filter_by(productId=_productId).first()
        product_to_update.comments = _comments
        db.session.commit()

    def replace_product(_productId, _productTitle, _price, _rating, _comments):
        product_to_replace = Product.query.filter_by(productId=_productId).first()
        product_to_replace.price = _price
        product_to_replace.productTitle = _productTitle
        product_to_replace.rating = _rating
        product_to_replace.comments = _comments
        db.session.commit()

    def __repr__(self):
        product_object = {
            'image_path': self.image_path,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'authorName': self.authorName,
            'publisher': self.publisher,
            'genre': self.genre
        }
        return json.dumps(product_object)

    def __str__(self):
        return f"{self.title}"

