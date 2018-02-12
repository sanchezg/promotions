from flask_restplus import reqparse

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('page', type=int, required=False, default=1,
                                  help='Page number')
pagination_arguments.add_argument('bool', type=bool, required=False, default=1,
                                  help='Page number')
pagination_arguments.add_argument('per_page', type=int, required=False,
                                  choices=[10, 20, 50, 100], default=10,
                                  help='Results per page {error_msg}')


# TODO: add an argument to filter by seller
promotion_filters = reqparse.RequestParser()
promotion_filters.add_argument('product', type=int, required=False,
                               default=None)
