import pandas as pd
from random import choice


def products_factory(amount):
    """Creates `amount` number of class::Product instances and returns them.
    The class::Seller instances used for products are randomly chosen from
    the sellers already created.
    """
    pass


def promotions_factory(amount):
    """Creates `amount` number of class::Promotion instances and returns them.
    The class::Product instances used for promotions are randomly chosen
    from the products already created.
    """
    pass


def sellers_factory(amount):
    """Creates `amount` number of class::Seller instances and returns them.
    """
    pass


def populate_DB(n_sellers=10, n_products=100, n_promotions=50):
    """Populates DB with an amount of `n_sellers` class:Seller instances,
    `n_products` class::Product instances and `n_promotions` class::Promotion
    instances.
    """
    pass
