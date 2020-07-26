# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#
# imports
from flask import json  # from sqlalchemy.orm import relationship, backref


# ----------------------------------------------------------------------------#
# Models core.
# ----------------------------------------------------------------------------#
from tedev.core.models.db_initializer import db
from tedev.core.utiles import edejsonnify, ejsonnify


# ----------------------------------------------------------------------------#
#
class myMixin:
    id                  = db.Column(db.Integer,     primary_key=True)
    firstname           = db.Column(db.String(),    nullable=False) #, unique=True)
    lastname            = db.Column(db.String(),    nullable=False) #, unique=True)
    city                = db.Column(db.String(120), nullable=False)
    state               = db.Column(db.String(120), nullable=False)
    phone               = db.Column(db.String(120), nullable=False)
    address             = db.Column(db.String(120), nullable=False)


#employees
class Participant(db.Model, myMixin):
    entity_name = 'participant'
    __tablename__ = 't' + entity_name

    email               = db.Column(db.String(120), nullable=False)
    entreprise          = db.Column(db.String(120))  # , nullable=False)

    #
    def __init__(self, entity=None):
        if entity: edejsonnify(self, entity)
    def __repr__(self): return json.dumps(ejsonnify('tedevB' ,self))

# ----------------------------------------------------------------------------#
#employees
class Employee(db.Model, myMixin):
    entity_name = 'employee'
    __tablename__ = 't' + entity_name

    email               = db.Column(db.String(120), nullable=False)
    entreprise          = db.Column(db.String(120))  # , nullable=False)

    #
    def __init__(self, entity=None):
        if entity: edejsonnify(self, entity)
    def __repr__(self): return json.dumps(ejsonnify('tedevB' ,self))


# ----------------------------------------------------------------------------#
Entities_tedev = { 'participant': Participant, 'employee': Employee }
