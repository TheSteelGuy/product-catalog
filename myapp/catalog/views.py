#myapp/catalogue/views.py
#coding:"utf-8"

#third party imports
from flask import request, jsonify

#local imports
from . import catalog
from .. import db
from ..models import Product,Category

@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."

#by default routes use GeT method
@catalog.route('/product/<int:id>')
def product(id):
    product = Product.query.get_or_404(id)
    return 'Product -{} is $ {}' .format(product.name, product.price)


@catalog.route('/products')
def products():
    products = Product.query.all()
    res = {}
    for product in products:
         res[product.id] = {
                    'name': product.name,
                    'price': product.price,
                    'category': product.category.name
         }
    return jsonify(res)


@catalog.route('/create-category', methods=['POST'])
def create_category():
    name = request.form.get('name')
    category = Category(name) 
    db.session.add(category)
    db.session.commit()       
    return 'Category created'

@catalog.route('/product-create', methods=['POST',])
def create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    category_name = request.form.get('category')
    category = Category.query.filter_by(name=category_name).first()
    product = Product(name, price,category)
    db.session.add(product)
    db.session.commit()
    return 'Product created.'
  
@catalog.route('/categories',methods=['GET'])
def get_categories():
    categories = Category.query.all()
    response = {}
    for category in categories:
        response[category.id]={
         'name' : category.name 
        }
        for product in category.products:
           response[category.id]['products'] = {
             'id': product.id,
             'name': product.name,
            'price': product.price
           }
    return jsonify(response)
    





































