"""CRUD functions for Product model.
"""

from promotions.database import db
from promotions.sales.models import Product, Seller


def new_product_item(data):
    """Creates a new product in DB with data uploaded by the user.
    """
    name = data.get('name', '')
    description = data.get('description', '')
    price = data.get('price', 0)
    seller_id = data.get('seller_id')
    seller = Seller.query.filter(Seller.id == seller_id).one()
    product = Product(name=name, description=description, price=price,
                      seller=seller)
    db.session.add(product)
    db.session.commit()


def update_product_item(product_id, data):
    """Updates product item data in DB.
    """
    product = Product.query.filter(Product.id == product_id).one()
    product.name = data.get('name', '')
    product.description = data.get('description', '')
    product.price = data.get('price', 0)
    seller_id = data.get('seller_id')
    product.seller = Seller.query.filter(Seller.id == seller_id).one()
    db.session.add(product)
    db.session.commit()


def delete_product_item(product_id):
    """Deletes from DB a product by id.
    """
    product = Product.query.filter(Product.id == product_id).one()
    db.session.delete(product)
    db.session.commit()
