# promotions
A simple REST API to expose Products and Promotions.

## Installation

Checkout this repo.
Create a virtualenv with python3.6, install MySQL, and inside the virtualenv run:

```
 $ pip install -r requirements.txt
```

## Configuration



## First steps

Inside a python interpreter, run the following commands:

```
 from promotions.database import reset_database
 from promotions.app import app, initialize_app

 initialize_app(app)

 with app.app_context():
     reset_database()

```

That will initialize the DB (by default SQLite).

If you receive some message like:

```
ModuleNotFoundError: No module named 'promotions'
```

Then, you will need to add the working directory to the PYTHONPATH environment variable:

```
export PYTHONPATH=.:$PYTHONPATH
```

## Example data

Load example data running:

```
promotions/sales/factories> python factories.py --sellers=S --products=P1 --promotions=P2
```

Where:
- S is the amount of sellers you want to create.
- P1 is the amount of products you want to create.
- P2 is the amount of promotions you want to create.

## Run

Run development server:

```
promotions> python app.py
```

And test the API with httpie:

```
$ http http://127.0.0.1:5000/api/sales/promotion/
```

Or with curl:

```
$ curl -X GET http://127.0.0.1:5000/api/sales/promotion/
```
