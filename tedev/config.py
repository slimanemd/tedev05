#
import os

#security key
SECRET_KEY = os.urandom(32)

# Enable debug mode.
DEBUG = True

# Grabs the folder where the script runs.
# basedir = os.path.abspath(os.path.dirname(__file__))

#
# Connect to the database # IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'sqlite:///data/databaseB.db'
#'postgres://slimed:Security93@localhost:5432/fyyur02'  #'sqlite:///example.db'
