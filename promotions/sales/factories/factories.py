"""Populate promotions DB.

Usage:
  factories.py [--sellers=<NSELL> [--products=<NPROD> [--promotions=<NPROM>]]]
  factories.py (-h | --help)

Options:
  -h --help     Show this screen.
  --sellers=<NSELL>     Creates NSELL amount of sellers [default=10]
  --products=<NPROD>    Creates NPROD amount of products [default=100]
  --promotions=<NPROM>  Creates NPROM amount of promotions [default=50]

"""

import pandas as pd
from docopt import docopt
from random import choice
from tqdm import tqdm
from promotions.app import app, initialize_app
from promotions.database import db
from promotions.sales.models import Seller, Product, Promotion


AMAZON_DATASET = 'amazon_toys_subset.csv'
DISCOUNTS = [0, 5, 10, 15, 25, 35, 50, 65, 75]


def products_factory(app, amount):
    """Creates `amount` number of class::Product instances and returns them.
    The class::Seller instances used for products are randomly chosen from
    the sellers already created.
    """
    products = []
    sample_df = load_dataset(sample=amount,
                             columns=['product_name', 'description', 'price'])
    with app.app_context():
        sellers = Seller.query.all()
    if not sellers:
        raise "There's no Sellers in DB, please populate with sellers before creating products"
    pbar = tqdm(sample_df.iterrows())
    for _, row in pbar:
        pbar.set_description("Creating products")
        p = Product()
        p.name = row['product_name']
        p.description = row['description']
        p.price = row['price']
        p.seller = choice(sellers)
        with app.app_context():
            db.session.add(p)
            db.session.commit()
        products.append(p)
    return products


def promotions_factory(amount):
    """Creates `amount` number of class::Promotion instances and returns them.
    The class::Product instances used for promotions are randomly chosen
    from the products already created.
    """
    promotions = []
    with app.app_context():
        products = Product.query.all()
    if not products:
        raise "There's no products in DB, please populate with products before creating promotions"
    pbar = tqdm(range(amount))
    for ix in pbar:
        pbar.set_description("Creating promotions")
        p = Promotion()
        p.product = choice(products)
        p.discount = choice(DISCOUNTS)
        p.shipping_discount = choice(DISCOUNTS)
        with app.app_context():
            db.session.add(p)
            db.session.commit()
        promotions.append(p)
    return promotions


def sellers_factory(app, amount):
    """Creates `amount` number of class::Seller instances and returns them.
    """
    sellers = []
    sample_df = load_dataset(sample=amount, columns=['sellers'])
    pbar = tqdm(sample_df.iterrows())
    for _, row in pbar:
        pbar.set_description("Creating sellers")
        s = Seller()
        try:
            s.name = row.get('sellers')
        except KeyError:
            continue
        else:
            with app.app_context():
                db.session.add(s)
                db.session.commit()
            sellers.append(s)
    return sellers


def populate(app, n_sellers=10, n_products=100, n_promotions=50):
    """Populates DB with an amount of `n_sellers` class:Seller instances,
    `n_products` class::Product instances and `n_promotions` class::Promotion
    instances.
    """
    import ipdb; ipdb.set_trace()
    sellers = sellers_factory(app, n_sellers)
    products = products_factory(app, n_products)
    promotions = promotions_factory(n_promotions)
    return sellers + products + promotions


def load_dataset(csv_file=AMAZON_DATASET, sample=None, columns=None):
    df = pd.read_csv(csv_file)
    if sample is not None:
        df = df.sample(n=sample)
    if columns is not None:
        df = df[columns]
    return df


if __name__ == '__main__':
    args = docopt(__doc__)
    n_sellers = int(args.get('--sellers'))
    n_products = int(args.get('--products'))
    n_promotions = int(args.get('--promotions'))
    initialize_app(app)
    populated = populate(app, n_sellers=n_sellers, n_products=n_products,
                         n_promotions=n_promotions)
    print("Succesfully created %d instances" % len(populated))
