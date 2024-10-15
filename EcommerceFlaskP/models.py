from settings import *
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# add the rating to product copy 
# add the total rating to product 
product_copy = db.Table('product_copy',
                    db.Column('id',db.Integer, primary_key=True),
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
                       )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    products = db.relationship('Product', secondary=product_copy, backref=db.backref('users', lazy='dynamic')) 
    ShippingAddress = db.Column(db.String(128))
    CreditCardNum = db.Column(db.String(128))
    ExpDate = db.Column(db.String(128))
    CVS = db.Column(db.Integer)
    NameOnCard = db.Column(db.String(128))

    def __str__(self):
        return self.name

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)

    def __str__(self):
        product = Product.query.get(self.product_id)
        return f"{product.title}"

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    data_storage_path = db.Column(db.String(128))
    genre = db.Column(db.String(128))
    title = db.Column(db.String(128))
    description = db.Column(db.String(128))
    price = db.Column(db.Float)
    maker = db.Column(db.String(128))
    platformType = db.Column(db.String(32))
    

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
            'maker': self.maker,
            'type': self.platformType,
        }
        return json.dumps(product_object)

    def __str__(self):
        return f"{self.title}"

class ProductRating(db.Model):
    __tablename__ = 'product_rating'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Integer)
    review = db.Column(db.String(512))

    product = db.relationship('Product', backref=db.backref('ratings', lazy='dynamic'))
    user = db.relationship('User', backref=db.backref('ratings', lazy='dynamic'))

    def __repr__(self):
        return f"<ProductRating {self.rating} for product {self.product_id} by user {self.user_id}>"

class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product_copy_id = db.Column(db.Integer, db.ForeignKey('product_copy.id'))

    def __str__(self):
        product = Product.query.get(self.product_id)
        return f"{product.title}"

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(128))