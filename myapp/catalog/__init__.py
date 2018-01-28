#myapp/catalog/__init__.py

#coding:"utf-8"

from flask import Blueprint

catalog = Blueprint('catalog',__name__)

from . import views
