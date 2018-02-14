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

## Example data



## Run


