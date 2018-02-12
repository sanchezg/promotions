"""Models for the Promotions app.
"""
from promotions.database import db, MAX_CHAR_LENGTH


class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_CHAR_LENGTH))

    def __repr__(self):
        return 'Seller "%r"' % self.name


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_CHAR_LENGTH))
    description = db.Column(db.String(MAX_CHAR_LENGTH))
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'))
    seller = db.relationship('Seller',
                             backref=db.backref('products', lazy='dynamic'))
    price = db.Column(db.Integer)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.seller = kwargs.get('seller')
        self.price = kwargs.get('price', 0)

    def __repr__(self):
        return 'Product "%r"' % self.name


class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product',
                              backref=db.backref('promotions', lazy='dynamic'))
    discount = db.Column(db.Integer, default=0)
    shipping_discount = db.Column(db.Integer, default=0)
