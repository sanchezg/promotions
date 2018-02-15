"""Views for the Promotions app.
"""
from flask import request
from flask_restplus import Resource
from promotions.sales.restplus import api
from promotions.sales.models import Product, Promotion
from promotions.sales.parsers import pagination_arguments, promotion_filters
from promotions.sales.serializers import (product_item, page_of_products,
                                          promotion_item, page_of_promotions)
from promotions.sales.products import (new_product_item, update_product_item,
                                       delete_product_item)
from promotions.sales.promotions import (new_promotion, update_promotion,
                                         delete_promotion)


ns = api.namespace('sales', description='Sales endpoints')


@ns.route('/product/')
class ProductCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_products)
    def get(self):
        """Returns list of products.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        query = Product.query
        products = query.paginate(page, per_page, error_out=False)

        return products

    @api.expect(product_item)
    def post(self):
        """Creates a new product.
        """
        new_product_item(request.json)
        return None, 201


@ns.route('/product/<int:id>')
@api.response(404, 'Product not found.')
class ProductItem(Resource):

    @api.marshal_with(product_item)
    def get(self, id):
        """Returns a product item.
        """
        return Product.query.filter(Product.id == id).one()

    @api.expect(product_item)
    @api.response(204, 'Product successfully updated.')
    def put(self, id):
        """Updates a product item.
        """
        data = request.json
        update_product_item(id, data)
        return None, 204

    @api.response(204, 'Product successfully deleted.')
    def delete(self, id):
        """Deletes a product item.
        """
        delete_product_item(id)
        return None, 204


@ns.route('/promotion/')
class PromotionCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_promotions)
    def get(self):
        """Returns list of promotions.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        query = Promotion.query
        promotions = query.paginate(page, per_page, error_out=False)

        return promotions

    @api.expect(promotion_item)
    def post(self):
        """Creates a new promotion.
        """
        new_promotion(request.json)
        return None, 201


@ns.route('/promotion/<int:id>')
@api.response(404, 'Promotion not found.')
class PromotionItem(Resource):

    @api.marshal_with(promotion_item)
    def get(self, id):
        """Returns a product item.
        """
        return Promotion.query.filter(Promotion.id == id).one()

    @api.expect(promotion_item)
    @api.response(204, 'Promotion successfully updated.')
    def put(self, id):
        """Updates a product item.
        """
        data = request.json
        update_promotion(id, data)
        return None, 204

    @api.response(204, 'Promotion successfully deleted.')
    def delete(self, id):
        """Deletes a product item.
        """
        delete_promotion(id)
        return None, 204
