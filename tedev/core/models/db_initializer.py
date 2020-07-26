#
from flask_sqlalchemy import SQLAlchemy

#
from tedev.config import SQLALCHEMY_DATABASE_URI

#
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path = SQLALCHEMY_DATABASE_URI):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
db_drop_and_create_all()
    drops the models tables and starts fresh
    can be used to initialize a clean models
'''


def db_drop_and_create_all(app_path = ""):    #db.drop_all()
    import os
    if os.path.isfile(app_path +  "/tedev/data/databaseB.db") :
        os.remove(app_path +  "/tedev/data/databaseB.db")
        print("DB File Removed!")
    db.create_all()

"""
-------------------------------------------------------------------------------
function    : populate_db
description : Helper function to populate the database
arguments   : data : data used to fill the different tables and fields in DB
              Entity : class of the associated entity
-------------------------------------------------------------------------------
Entities Classes
data json object repre Entity in Entities
    Entities = { 'key_entityX': EntityX, 'key_entityY': EntityY, ...}
    data = [
    {
        'key_entityX': [
            {  instanceX1 },
            {  instanceX2 },
            ..]
    }
    ....
    ]

4x  Entities = { 'drink':Drink, 'user':User}
    data = { 'drink' : [ { 'title': 'T1', 'parts':2 }, { 'title': 'T2', 'parts':3 } ] ,
    'user' :  [ { 'name': 'Ali', 'age':21 }, { 'name': 'Omar', 'age':35 } ]}

"""
def populate_db(data, Entities, reset=False, app_path=""):
    if reset:
        db_drop_and_create_all(app_path)

    for key,value in data.items():
        cll_entities = []
        for entity in value:
            entity.pop("id", None)
            e = Entities[key](entity)
            cll_entities.append(e)

        db.session.add_all(cll_entities)
        db.session.commit()

"""
-------------------------------------------------------------------------------
function    : get_max_id
description : helper function to get the max id in table of the entity
arguments   : table_col : table column
-------------------------------------------------------------------------------
"""

def get_max_id(table_col):
    from sqlalchemy.sql.expression import func
    return db.session.query(func.max(table_col)).scalar()


"""
-------------------------------------------------------------------------------
"""
