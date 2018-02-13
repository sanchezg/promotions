"""CRUD functions for Promotion model.
"""

from promotions.database import db
from promotions.sales.models import Product, Promotion


def new_promotion(data):
    """Creates a new promotion in DB with data uploaded by the user.
    """
    promotion = Promotion()
    promotion.discount = data.get('discount', 0)
    promotion.shipping_discount = data.get('shipping_discount', 0)
    product_id = data.get('product_id')
    promotion.product = Product.query.filter(Product.id == product_id).one()
    db.session.add(promotion)
    db.session.commit()


def update_promotion(promotion_id, data):
    """Updates promotion data in DB.
    """
    promotion = Promotion.query.filter(Promotion.id == promotion_id).one()
    promotion.discount = data.get('discount', 0)
    promotion.shipping_discount = data.get('shipping_discount', 0)
    product_id = data.get('product_id')
    promotion.product = Product.query.filter(Product.id == product_id).one()
    db.session.add(promotion)
    db.session.commit()


def delete_promotion(promotion_id):
    """Deletes from DB a promotion by id.
    """
    promotion = Promotion.query.filter(Promotion.id == promotion_id).one()
    db.session.delete(promotion)
    db.session.commit()
