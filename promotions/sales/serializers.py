from flask_restplus import fields
from promotions.sales.restplus import api

product_item = api.model('Product item', {
    'id': fields.Integer(readOnly=True,
                         description='Product item unique identifier'),
    'name': fields.String(required=True, description='Product name'),
    'description': fields.String(required=True,
                                 description='Product description'),
    'seller_id': fields.Integer(description='Seller id'),
    'seller': fields.String(attribute='seller.name'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(
        description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_products = api.inherit('Page of products', pagination, {
    'items': fields.List(fields.Nested(product_item))
})

promotion_item = api.model('Promotion', {
    'id': fields.Integer(readOnly=True,
                         description='Promotion unique identifier'),
    'discount': fields.Integer(description='Price discount'),
    'shipping_discount': fields.Integer(description='Shipping discount'),
    'product_id': fields.Integer(description='Product id'),
    'product': fields.String(attribute='product.name')
})

page_of_promotions = api.inherit('Page of promotions', pagination, {
    'promotions': fields.List(fields.Nested(promotion_item))
})
