from flask_sqlalchemy import SQLAlchemy


MAX_CHAR_LENGTH = 255

db = SQLAlchemy()


def reset_database():
    from promotions.sales.models import Seller, Product, Promotion  # noqa
    db.drop_all()
    db.create_all()
