
import os

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/catalog_db"
SECRET_KEY = os.urandom(24)
