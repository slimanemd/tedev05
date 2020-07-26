from flask import Flask


# initialization
from tedev.config import SECRET_KEY, SQLALCHEMY_DATABASE_URI

from tedev.core.models.db_initializer import db, setup_db
from  tedev.core.models.model_tedevB import Participant, Employee

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    setup_db(app)

    return app

#
app = create_app()

#
from tedev.core.routes import *

#
if __name__ == "__main__":
    app.run()